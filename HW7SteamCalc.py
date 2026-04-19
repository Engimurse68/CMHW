# -*- coding: utf-8 -*-
#region imports
import sys
from pyXSteam.XSteam import XSteam
from PyQt6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout,
                             QGroupBox, QGridLayout, QLabel, QLineEdit,
                             QComboBox, QPushButton, QRadioButton, QSizePolicy,
                             QSpacerItem, QScrollArea)
from PyQt6.QtCore import Qt
from scipy.optimize import fsolve
#endregion

# Unit conversions, Si <> English
class UC:
    psi_to_bar = 1.0 / 14.5038
    bar_to_psi = 1.0 / psi_to_bar
    ft_to_m = 1.0 / 3.28084
    ft3_to_m3 = ft_to_m ** 3
    lbf_to_kg = 1.0 / 2.20462
    ft3perlb_to_m3perkg = ft3_to_m3 / lbf_to_kg
    m3perkg_to_ft3perlb = 1.0 / ft3perlb_to_m3perkg
    kJ_to_btu = 1.0 / 1.05506
    btu_to_kJ = 1.0 / kJ_to_btu
    kg_to_lbf = 1.0 / lbf_to_kg
    kJperkg_to_btuperlb = kJ_to_btu / kg_to_lbf
    btuperlb_to_kJperkg = 1.0 / kJperkg_to_btuperlb
    btuperlbF_to_kJperkgC = 4.1868
    kJperkgC_to_btuperlbF = 1.0 / btuperlbF_to_kJperkgC

    @classmethod
    def C_to_F(cls, T): return T * 9.0 / 5.0 + 32
    @classmethod
    def F_to_C(cls, T): return (T - 32) * 5.0 / 9.0


# ── Thermodynamic helper classes (unchanged from original) ───────────────────
class thermoSatProps:
    def __init__(self, p=None, t=None, SI=True):
        self.steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS)
        if p is not None:
            self.getSatProps(p, SI)
        elif t is not None:
            self.getSatProps(self.steamTable.psat_t(t), SI)

    def getSatProps(self, p, SI=True):
        self.steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS if SI else XSteam.UNIT_SYSTEM_FLS)
        self.pSat = p
        self.tSat = self.steamTable.tsat_p(p)
        self.vf = self.steamTable.vL_p(p)
        self.vg = self.steamTable.vV_p(p)
        self.hf = self.steamTable.hL_p(p)
        self.hg = self.steamTable.hV_p(p)
        self.uf = self.steamTable.uL_p(p)
        self.ug = self.steamTable.uV_p(p)
        self.sf = self.steamTable.sL_p(p)
        self.sg = self.steamTable.sV_p(p)
        self.vgf = self.vg - self.vf
        self.hgf = self.hg - self.hf
        self.sgf = self.sg - self.sf
        self.ugf = self.ug - self.uf


class thermoState:
    def __init__(self, p=None, t=None, v=None, u=None, h=None, s=None, x=None):
        self.steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS)
        self.region = "saturated"
        self.p = p; self.t = t; self.v = v
        self.u = u; self.h = h; self.s = s; self.x = x

    def computeProperties(self):
        if self.region == "two-phase":
            self.u = self.steamTable.uL_p(self.p) + self.x * (self.steamTable.uV_p(self.p) - self.steamTable.uL_p(self.p))
            self.h = self.steamTable.hL_p(self.p) + self.x * (self.steamTable.hV_p(self.p) - self.steamTable.hL_p(self.p))
            self.s = self.steamTable.sL_p(self.p) + self.x * (self.steamTable.sV_p(self.p) - self.steamTable.sL_p(self.p))
            self.v = self.steamTable.vL_p(self.p) + self.x * (self.steamTable.vV_p(self.p) - self.steamTable.vL_p(self.p))
        else:
            self.u = self.steamTable.u_pt(self.p, self.t)
            self.h = self.steamTable.h_pt(self.p, self.t)
            self.s = self.steamTable.s_pt(self.p, self.t)
            self.v = self.steamTable.v_pt(self.p, self.t)
            self.x = 1.0 if self.region == "super-heated vapor" else 0.0

    def clamp(self, x, low, high):
        return max(low, min(high, x))

    def between(self, x, low, high):
        return low <= x <= high

    def setState(self, stProp1, stProp2, stPropVal1, stPropVal2, SI=True):
        self.steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS if SI else XSteam.UNIT_SYSTEM_FLS)
        SP = [stProp1.lower(), stProp2.lower()]
        f1 = float(stPropVal1)
        f2 = float(stPropVal2)

        if SP[0] == 'p' or SP[1] == 'p':
            oFlipped = SP[0] != 'p'
            SP1 = SP[0] if oFlipped else SP[1]
            self.p = f1 if not oFlipped else f2
            tSat = self.steamTable.tsat_p(self.p)
            if SP1 == 't':
                self.t = f2 if not oFlipped else f1
                tSat = round(tSat)
                if self.t < tSat or self.t > tSat:
                    self.region = "sub-cooled liquid" if self.t < tSat else "super-heated vapor"
                else:
                    self.region = "two-phase"; self.x = 0.5
            elif SP1 == 'v':
                self.v = f2 if not oFlipped else f1
                vf = round(self.steamTable.vL_p(self.p), 5)
                vg = round(self.steamTable.vV_p(self.p), 3)
                if self.v < vf or self.v > vg:
                    self.region = "sub-cooled liquid" if self.v < vf else "super-heated vapor"
                    dt = 1.0 if self.v > vg else -1.0
                    fn1 = lambda T: self.v - self.steamTable.v_pt(self.p, T)
                    self.t = fsolve(fn1, [tSat + dt])[0]
                else:
                    self.region = "two-phase"
                    vgf = vg - vf
                    self.x = (self.v - vf) / vgf; self.t = tSat
            elif SP1 == 'u':
                self.u = f2 if not oFlipped else f1
                uf = round(self.steamTable.uL_p(self.p), 5)
                ug = round(self.steamTable.uV_p(self.p), 3)
                ugf = ug - uf
                if self.u < uf or self.u > ug:
                    self.region = "sub-cooled liquid" if self.u < uf else "super-heated vapor"
                    dt = 1.0 if self.u > ug else -1.0
                    fn3 = lambda T: self.u - self.steamTable.u_pt(self.p, T)
                    self.t = fsolve(fn3, [tSat + dt])[0]
                else:
                    self.region = "two-phase"
                    self.x = (self.u - uf) / ugf; self.t = tSat
            elif SP1 == 'h':
                self.h = f2 if not oFlipped else f1
                hf = self.steamTable.hL_p(self.p)
                hg = self.steamTable.hV_p(self.p)
                hgf = hg - hf
                if self.h < hf or self.h > hg:
                    self.region = "sub-cooled liquid" if self.h < hf else "super-heated vapor"
                    self.t = self.steamTable.t_ph(self.p, self.h)
                else:
                    self.region = "two-phase"
                    self.x = (self.h - hf) / hgf; self.t = tSat
            elif SP1 == 's':
                self.s = f2 if not oFlipped else f1
                sf = self.steamTable.sL_p(self.p)
                sg = self.steamTable.sV_p(self.p)
                sgf = sg - sf
                if self.s < sf or self.s > sg:
                    self.region = "sub-cooled liquid" if self.s < sf else "super-heated vapor"
                    self.t = self.steamTable.t_ps(self.p, self.s)
                else:
                    self.region = "two-phase"
                    self.x = (self.s - sf) / sgf; self.t = tSat
            elif SP1 == 'x':
                self.region = "two-phase"
                self.x = f2 if not oFlipped else f1
                self.t = tSat

        elif SP[0] == 't' or SP[1] == 't':
            oFlipped = SP[0] != 't'
            SP1 = SP[0] if oFlipped else SP[1]
            self.t = f1 if not oFlipped else f2
            pSat = self.steamTable.psat_t(self.t)
            if SP1 == 'v':
                self.v = f2 if not oFlipped else f1
                vf = self.steamTable.vL_p(pSat); vg = self.steamTable.vV_p(pSat)
                if self.v < vf or self.v > vg:
                    self.region = "sub-cooled liquid" if self.v < vf else "super-heated vapor"
                    dp = -0.1 if self.v > vg else 0.1
                    fn = lambda P: [self.v - self.steamTable.v_pt(P, self.t)]
                    self.p = fsolve(fn, [pSat + dp])[0]
                else:
                    self.region = "two-phase"; self.x = (self.v - vf) / (vg - vf); self.p = pSat
            elif SP1 == 'u':
                self.u = f2 if not oFlipped else f1
                uf = self.steamTable.uL_p(pSat); ug = self.steamTable.uV_p(pSat)
                if self.u < uf or self.u > ug:
                    self.region = "sub-cooled liquid" if self.u < uf else "super-heated vapor"
                    dp = 0.1 if self.u > ug else -0.1
                    fn = lambda P: self.u - self.steamTable.u_pt(self.t, P)
                    self.p = fsolve(fn, [pSat + dp])[0]
                else:
                    self.region = "two-phase"; self.x = (self.u - uf) / (ug - uf); self.p = pSat
            elif SP1 == 'h':
                self.h = f2 if not oFlipped else f1
                hf = self.steamTable.hL_p(pSat); hg = self.steamTable.hV_p(pSat)
                if self.h < hf or self.h > hg:
                    self.region = "sub-cooled liquid" if self.h < hf else "super-heated vapor"
                    self.p = self.steamTable.p_th(self.t, self.h)
                else:
                    self.region = "two-phase"; self.x = (self.h - hf) / (hg - hf); self.p = pSat
            elif SP1 == 's':
                self.s = f2 if not oFlipped else f1
                sf = self.steamTable.sL_p(pSat); sg = self.steamTable.sV_p(pSat)
                if self.s < sf or self.s > sg:
                    self.region = "sub-cooled liquid" if self.s < sf else "super-heated vapor"
                    self.p = self.steamTable.p_ts(self.t, self.s)
                else:
                    self.region = "two-phase"; self.x = (self.s - sf) / (sg - sf); self.p = pSat
            elif SP1 == 'x':
                self.x = f2 if not oFlipped else f1
                self.region = "two-phase"; self.p = pSat

        elif SP[0] == 'v' or SP[1] == 'v':
            oFlipped = SP[0] != 'v'
            SP1 = SP[0] if oFlipped else SP[1]
            self.v = f1 if not oFlipped else f2
            if SP1 == 'h':
                self.h = f2 if not oFlipped else f1
                def fn12(P):
                    hf = self.steamTable.hL_p(P); hg = self.steamTable.hV_p(P)
                    vf = self.steamTable.vL_p(P); vg = self.steamTable.vV_p(P)
                    if self.between(self.h, hf, hg):
                        x = (self.h - hf) / (hg - hf)
                        return self.v - (vf + x * (vg - vf))
                    return self.v - self.steamTable.v_ph(P, self.h)
                self.p = fsolve(fn12, [1.0])[0]
                vf = self.steamTable.vL_p(self.p); vg = self.steamTable.vV_p(self.p)
                tsat = self.steamTable.tsat_p(self.p)
                if self.v < vf or self.v > vg:
                    self.region = "sub-cooled liquid" if self.v < vf else "super-heated vapor"
                    dt = -1 if self.v < vf else 1
                    self.t = fsolve(lambda t: self.v - self.steamTable.v_pt(self.p, t), [tsat + dt])[0]
                else:
                    self.region = "two-phase"; self.t = tsat; self.x = (self.v - vf) / (vg - vf)
            elif SP1 == 'u':
                self.u = f2 if not oFlipped else f1
                def fn13(PT):
                    p, t = PT
                    uf = self.steamTable.uL_p(p); ug = self.steamTable.uV_p(p)
                    vf = self.steamTable.vL_p(p); vg = self.steamTable.vV_p(p)
                    if self.between(self.u, uf, ug):
                        x = (self.u - uf) / (ug - uf)
                        return [self.v - (vf + x * (vg - vf)), 0]
                    return [self.v - self.steamTable.v_pt(p, t), self.u - self.steamTable.u_pt(p, t)]
                props = fsolve(fn13, [1, 100])
                self.p = props[0]; self.t = props[1]
                uf = self.steamTable.uL_p(self.p); ug = self.steamTable.uV_p(self.p)
                if self.u < uf or self.u > ug:
                    self.region = "sub-cooled liquid" if self.u < uf else "super-heated vapor"
                else:
                    self.region = "two-phase"; self.x = (self.u - uf) / (ug - uf)
            elif SP1 == 's':
                self.s = f2 if not oFlipped else f1
                def fn14(PT):
                    p, t = PT
                    sf = self.steamTable.sL_p(p); sg = self.steamTable.sV_p(p)
                    vf = self.steamTable.vL_p(p); vg = self.steamTable.vV_p(p)
                    if self.between(self.s, sf, sg):
                        x = (self.s - sf) / (sg - sf)
                        return [self.v - vf - x * (vg - vf), 0.0]
                    return [self.v - self.steamTable.v_pt(p, t), self.s - self.steamTable.s_pt(p, t)]
                props = fsolve(fn14, [1, 100])
                self.p = props[0]; self.t = props[1]
                sf = self.steamTable.sL_p(self.p); sg = self.steamTable.sV_p(self.p)
                if self.s < sf or self.s > sg:
                    self.region = "sub-cooled liquid" if self.s < sf else "super-heated vapor"
                else:
                    self.region = "two-phase"; self.x = (self.s - sf) / (sg - sf)
            elif SP1 == 'x':
                self.x = self.clamp(f2 if not oFlipped else f1, 0, 1)
                self.region = "two-phase"
                def fn15(p):
                    vf = self.steamTable.vL_p(p); vg = self.steamTable.vV_p(p)
                    return self.v - (vf + self.x * (vg - vf))
                self.p = fsolve(fn15, [1])[0]
                self.t = self.steamTable.tsat_p(self.p)

        elif SP[0] == 'h' or SP[1] == 'h':
            oFlipped = SP[0] != 'h'
            SP1 = SP[0] if oFlipped else SP[1]
            self.h = f1 if not oFlipped else f2
            if SP1 == 'u':
                self.u = f2 if not oFlipped else f1
                def fn16(PT):
                    p, t = PT
                    hf = self.steamTable.hL_p(p); hg = self.steamTable.hV_p(p)
                    uf = self.steamTable.uL_p(p); ug = self.steamTable.uV_p(p)
                    if self.between(self.h, hf, hg):
                        x = (self.h - hf) / (hg - hf)
                        return [self.u - uf - x * (ug - uf), 0.0]
                    return [self.h - self.steamTable.h_pt(p, t), self.u - self.steamTable.u_pt(p, t)]
                props = fsolve(fn16, [1, 100])
                self.p = props[0]; self.t = props[1]
                hf = self.steamTable.hL_p(self.p); hg = self.steamTable.hV_p(self.p)
                if self.h < hf or self.h > hg:
                    self.region = "sub-cooled liquid" if self.h < hf else "super-heated vapor"
                else:
                    self.region = "two-phase"; self.x = (self.h - hf) / (hg - hf)
            elif SP1 == 's':
                self.s = f2 if not oFlipped else f1
                def fn17(PT):
                    p, t = PT
                    sf = self.steamTable.sL_p(p); sg = self.steamTable.sV_p(p)
                    hf = self.steamTable.hL_p(p); hg = self.steamTable.hV_p(p)
                    if self.between(self.s, sf, sg):
                        x = (self.s - sf) / (sg - sf)
                        return [self.h - hf - x * (hg - hf), 0.0]
                    return [self.h - self.steamTable.h_pt(p, t), self.s - self.steamTable.s_pt(p, t)]
                props = fsolve(fn17, [1, 100])
                self.p = props[0]; self.t = props[1]
                sf = self.steamTable.sL_p(self.p); sg = self.steamTable.sV_p(self.p)
                if self.s < sf or self.s > sg:
                    self.region = "sub-cooled liquid" if self.s < sf else "super-heated vapor"
                else:
                    self.region = "two-phase"; self.x = (self.s - sf) / (sg - sf)
            elif SP1 == 'x':
                self.x = self.clamp(f2 if not oFlipped else f1, 0, 1)
                self.region = "two-phase"
                def fn18(p):
                    hf = self.steamTable.hL_p(p); hg = self.steamTable.hV_p(p)
                    return self.h - (hf + self.x * (hg - hf))
                self.p = fsolve(fn18, [1])[0]
                self.t = self.steamTable.tsat_p(self.p)

        elif SP[0] == 'u' or SP[1] == 'u':
            oFlipped = SP[0] != 'u'
            SP1 = SP[0] if oFlipped else SP[1]
            self.u = f1 if not oFlipped else f2
            if SP1 == 's':
                self.s = f2 if not oFlipped else f1
                def fn19(PT):
                    p, t = PT
                    sf = self.steamTable.sL_p(p); sg = self.steamTable.sV_p(p)
                    uf = self.steamTable.uL_p(p); ug = self.steamTable.uV_p(p)
                    if self.between(self.s, sf, sg):
                        x = (self.s - sf) / (sg - sf)
                        return [self.u - uf - x * (ug - uf), 0.0]
                    return [self.u - self.steamTable.u_pt(p, t), self.s - self.steamTable.s_pt(p, t)]
                props = fsolve(fn19, [1, 100])
                self.p = props[0]; self.t = props[1]
                sf = self.steamTable.sL_p(self.p); sg = self.steamTable.sV_p(self.p)
                if self.s < sf or self.s > sg:
                    self.region = "sub-cooled liquid" if self.s < sf else "super-heated vapor"
                else:
                    self.region = "two-phase"; self.x = (self.s - sf) / (sg - sf)
            elif SP1 == 'x':
                self.x = self.clamp(f2 if not oFlipped else f1, 0, 1)
                self.region = "two-phase"
                def fn20(p):
                    uf = self.steamTable.uL_p(p); ug = self.steamTable.uV_p(p)
                    return self.u - (uf + self.x * (ug - uf))
                self.p = fsolve(fn20, [1])[0]
                self.t = self.steamTable.tsat_p(self.p)

        elif SP[0] == 's' or SP[1] == 's':
            oFlipped = SP[0] != 's'
            SP1 = SP[0] if oFlipped else SP[1]
            self.s = f1 if not oFlipped else f2
            if SP1 == 'x':
                self.x = self.clamp(f2 if not oFlipped else f1, 0, 1)
                self.region = "two-phase"
                def fn21(p):
                    sf = self.steamTable.sL_p(p); sg = self.steamTable.sV_p(p)
                    return self.s - (sf + self.x * (sg - sf))
                self.p = fsolve(fn21, [1])[0]
                self.t = self.steamTable.tsat_p(self.p)

        self.computeProperties()


# ── Single-state input panel ─────────────────────────────────────────────────
class StateInputPanel(QGroupBox):
    PROPS = ["Pressure (p)", "Temperature (T)", "Quality (x)",
             "Specific Internal Energy (u)", "Specific Enthalpy (h)",
             "Specific Volume (v)", "Specific Entropy (s)"]

    def __init__(self, title, default_val1="1.0", default_val2="100.0",
                 default_idx1=0, default_idx2=1):
        super().__init__(title)
        self._build(default_val1, default_val2, default_idx1, default_idx2)

    def _build(self, dv1, dv2, di1, di2):
        grid = QGridLayout(self)
        grid.addWidget(QLabel("Property 1"), 0, 0)
        grid.addWidget(QLabel("Property 2"), 0, 2)

        self.cmb1 = QComboBox(); self.cmb1.addItems(self.PROPS); self.cmb1.setCurrentIndex(di1)
        self.cmb2 = QComboBox(); self.cmb2.addItems(self.PROPS); self.cmb2.setCurrentIndex(di2)
        grid.addWidget(self.cmb1, 1, 0)
        grid.addWidget(self.cmb2, 1, 2)

        self.le1 = QLineEdit(dv1)
        self.le2 = QLineEdit(dv2)
        grid.addWidget(self.le1, 2, 0)
        grid.addWidget(self.le2, 2, 2)

        self.lbl_units1 = QLabel("")
        self.lbl_units2 = QLabel("")
        grid.addWidget(self.lbl_units1, 2, 1)
        grid.addWidget(self.lbl_units2, 2, 3)

        self.lbl_warning = QLabel("")
        self.lbl_warning.setStyleSheet("color: red;")
        grid.addWidget(self.lbl_warning, 3, 0, 1, 4)

    def get_prop_key(self, cmb):
        txt = cmb.currentText()
        return txt[txt.index('(')+1 : txt.index(')')]

    @property
    def prop1_key(self): return self.get_prop_key(self.cmb1)
    @property
    def prop2_key(self): return self.get_prop_key(self.cmb2)
    @property
    def val1(self): return self.le1.text()
    @property
    def val2(self): return self.le2.text()


# ── Main window ──────────────────────────────────────────────────────────────
class main_window(QWidget):
    PROP_ITEMS = ["Pressure (p)", "Temperature (T)", "Quality (x)",
                  "Specific Internal Energy (u)", "Specific Enthalpy (h)",
                  "Specific Volume (v)", "Specific Entropy (s)"]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thermodynamic State Calculator")
        self.currentUnits = 'SI'
        self._build_ui()
        self._connect_signals()
        self._set_units()
        self.show()

    # ── UI construction ──────────────────────────────────────────────────────
    def _build_ui(self):
        root = QVBoxLayout(self)

        # ── Units group ──
        grp_units = QGroupBox("System of Units")
        hl_units = QHBoxLayout(grp_units)
        self.rdo_SI = QRadioButton("SI"); self.rdo_SI.setChecked(True)
        self.rdo_EN = QRadioButton("English")
        hl_units.addWidget(self.rdo_SI); hl_units.addWidget(self.rdo_EN)
        root.addWidget(grp_units)

        # ── Specified Properties group ──
        grp_spec = QGroupBox("Specified Properties")
        spec_layout = QVBoxLayout(grp_spec)

        states_row = QHBoxLayout()
        self.state1_panel = StateInputPanel("State 1:")
        self.state2_panel = StateInputPanel("State 2:")
        states_row.addWidget(self.state1_panel)
        states_row.addWidget(self.state2_panel)
        spec_layout.addLayout(states_row)

        self.btn_calc = QPushButton("Calculate")
        self.btn_calc.setMinimumHeight(36)
        spec_layout.addWidget(self.btn_calc)
        root.addWidget(grp_spec)

        # ── State Properties group ──
        grp_results = QGroupBox("State Properties")
        results_row = QHBoxLayout(grp_results)

        self.grp_state1_out = QGroupBox("State 1")
        vl1 = QVBoxLayout(self.grp_state1_out)
        self.lbl_out1 = QLabel("—"); self.lbl_out1.setAlignment(Qt.AlignmentFlag.AlignTop)
        vl1.addWidget(self.lbl_out1)

        self.grp_state2_out = QGroupBox("State 2")
        vl2 = QVBoxLayout(self.grp_state2_out)
        self.lbl_out2 = QLabel("—"); self.lbl_out2.setAlignment(Qt.AlignmentFlag.AlignTop)
        vl2.addWidget(self.lbl_out2)

        self.grp_delta_out = QGroupBox("State Change (2 − 1)")
        vl3 = QVBoxLayout(self.grp_delta_out)
        self.lbl_out_delta = QLabel("—"); self.lbl_out_delta.setAlignment(Qt.AlignmentFlag.AlignTop)
        vl3.addWidget(self.lbl_out_delta)

        results_row.addWidget(self.grp_state1_out)
        results_row.addWidget(self.grp_state2_out)
        results_row.addWidget(self.grp_delta_out)
        root.addWidget(grp_results)
        root.addStretch()
        self.resize(900, 620)

    def _connect_signals(self):
        self.rdo_SI.clicked.connect(self._set_units)
        self.rdo_EN.clicked.connect(self._set_units)
        self.state1_panel.cmb1.currentIndexChanged.connect(self._set_units)
        self.state1_panel.cmb2.currentIndexChanged.connect(self._set_units)
        self.state2_panel.cmb1.currentIndexChanged.connect(self._set_units)
        self.state2_panel.cmb2.currentIndexChanged.connect(self._set_units)
        self.btn_calc.clicked.connect(self._calculate)

    # ── Units management ─────────────────────────────────────────────────────
    def _set_units(self):
        SI = self.rdo_SI.isChecked()
        newUnits = 'SI' if SI else 'EN'
        unit_changed = self.currentUnits != newUnits
        self.currentUnits = newUnits

        if SI:
            self.p_u = "bar"; self.t_u = "C"; self.u_u = "kJ/kg"
            self.h_u = "kJ/kg"; self.s_u = "kJ/(kg·C)"; self.v_u = "m³/kg"
        else:
            self.p_u = "psi"; self.t_u = "F"; self.u_u = "btu/lb"
            self.h_u = "btu/lb"; self.s_u = "btu/(lb·F)"; self.v_u = "ft³/lb"

        for panel in (self.state1_panel, self.state2_panel):
            self._update_panel_units(panel, SI, unit_changed)

    def _prop_unit(self, prop_text):
        if   'Pressure'    in prop_text: return self.p_u
        elif 'Temperature' in prop_text: return self.t_u
        elif 'Energy'      in prop_text: return self.u_u
        elif 'Enthalpy'    in prop_text: return self.h_u
        elif 'Entropy'     in prop_text: return self.s_u
        elif 'Volume'      in prop_text: return self.v_u
        else: return ""  # Quality

    def _convert_value(self, val, prop_text, to_SI):
        if   'Pressure'    in prop_text:
            return val * UC.psi_to_bar if to_SI else val * UC.bar_to_psi
        elif 'Temperature' in prop_text:
            return UC.F_to_C(val) if to_SI else UC.C_to_F(val)
        elif 'Energy'      in prop_text:
            return val * UC.btuperlb_to_kJperkg if to_SI else val * UC.kJperkg_to_btuperlb
        elif 'Enthalpy'    in prop_text:
            return val * UC.btuperlb_to_kJperkg if to_SI else val * UC.kJperkg_to_btuperlb
        elif 'Entropy'     in prop_text:
            return val * UC.btuperlbF_to_kJperkgC if to_SI else val * UC.kJperkgC_to_btuperlbF
        elif 'Volume'      in prop_text:
            return val * UC.ft3perlb_to_m3perkg if to_SI else val * UC.m3perkg_to_ft3perlb
        return val  # Quality — dimensionless

    def _update_panel_units(self, panel, SI, unit_changed):
        txt1 = panel.cmb1.currentText(); txt2 = panel.cmb2.currentText()
        panel.lbl_units1.setText(self._prop_unit(txt1))
        panel.lbl_units2.setText(self._prop_unit(txt2))
        if unit_changed:
            try:
                v1 = float(panel.le1.text())
                panel.le1.setText("{:.3f}".format(self._convert_value(v1, txt1, SI)))
            except ValueError: pass
            try:
                v2 = float(panel.le2.text())
                panel.le2.setText("{:.3f}".format(self._convert_value(v2, txt2, SI)))
            except ValueError: pass

    # ── Calculation ──────────────────────────────────────────────────────────
    def _make_label(self, st):
        lns = [
            "Region = {}".format(st.region),
            "p = {:.4f} ({})".format(st.p, self.p_u),
            "T = {:.4f} ({})".format(st.t, self.t_u),
            "u = {:.4f} ({})".format(st.u, self.u_u),
            "h = {:.4f} ({})".format(st.h, self.h_u),
            "s = {:.6f} ({})".format(st.s, self.s_u),
            "v = {:.6f} ({})".format(st.v, self.v_u),
            "x = {:.4f}".format(st.x if st.x is not None else float('nan')),
        ]
        return "\n".join(lns)

    def _make_delta_label(self, s1, s2):
        def d(a, b): return b - a if (a is not None and b is not None) else float('nan')
        lns = [
            "Δp = {:.4f} ({})".format(d(s1.p, s2.p), self.p_u),
            "ΔT = {:.4f} ({})".format(d(s1.t, s2.t), self.t_u),
            "Δu = {:.4f} ({})".format(d(s1.u, s2.u), self.u_u),
            "Δh = {:.4f} ({})".format(d(s1.h, s2.h), self.h_u),
            "Δs = {:.6f} ({})".format(d(s1.s, s2.s), self.s_u),
            "Δv = {:.6f} ({})".format(d(s1.v, s2.v), self.v_u),
        ]
        return "\n".join(lns)

    def _calculate(self):
        SI = self.rdo_SI.isChecked()
        results = []
        states = []
        for panel in (self.state1_panel, self.state2_panel):
            k1 = panel.prop1_key; k2 = panel.prop2_key
            if k1 == k2:
                panel.lbl_warning.setText("⚠ Cannot specify the same property twice.")
                return
            panel.lbl_warning.setText("")
            try:
                st = thermoState()
                st.setState(k1, k2, panel.val1, panel.val2, SI)
                states.append(st)
                results.append(self._make_label(st))
            except Exception as e:
                results.append("Error: {}".format(e))
                states.append(None)

        self.lbl_out1.setText(results[0])
        self.lbl_out2.setText(results[1])
        if states[0] is not None and states[1] is not None:
            self.lbl_out_delta.setText(self._make_delta_label(states[0], states[1]))
        else:
            self.lbl_out_delta.setText("—")


# ── Entry point ──────────────────────────────────────────────────────────────
def main():
    app = QApplication.instance() or QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    win = main_window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
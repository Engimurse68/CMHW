#region imports
from Air import *
from matplotlib import pyplot as plt
from PySide6 import QtWidgets as qtw
from copy import deepcopy as dc
import sys
#endregion

#region class definitions
class dualCycleModel():
    def __init__(self, p_initial=1E5, v_cylinder=3E-3, t_initial=300, pressure_ratio=1.5, cutoff=1.2, ratio=18.0, name='Air Standard Dual Cycle'):
        """
        Constructor for an air standard dual cycle. The Dual has 5 primary states:
        1. Isentropic compression from State 1 (BDC) to State 2 (TDC): v2 = v1/r
        2. Constant volume heat addition from State 2 to State 3: P3 = rp*P2, v3 = v2
        3. Constant pressure heat addition from State 3 to State 4: P4 = P3, v4 = rc*v3
        4. Isentropic expansion from State 4 to State 5 (BDC): v5 = v1
        5. Constant volume heat rejection from State 5 to State 1
        :param p_initial: Pressure in Pa
        :param v_cylinder: Volume in m^3
        :param t_initial: Initial temperature in K
        :param pressure_ratio: rp = P3/P2 (constant volume pressure ratio)
        :param cutoff: rc = v4/v3 (cutoff ratio for constant pressure heat addition)
        :param ratio: r = v1/v2 (compression ratio)
        """
        self.units = units()
        self.units.SI = False
        self.units.changed = False
        self.air = air()
        self.air.set(P=p_initial, T=t_initial)
        self.p_initial = p_initial
        self.T_initial = t_initial
        self.Ratio = ratio
        self.PressureRatio = pressure_ratio  # rp = P3/P2
        self.Cutoff = cutoff                 # rc = v4/v3
        self.V_Cylinder = v_cylinder
        self.air.n = self.V_Cylinder / self.air.State.v
        self.air.m = self.air.n * self.air.MW

        self.State1 = self.air.set(P=self.p_initial, T=self.T_initial)
        self.State2 = self.air.set(v=self.State1.v / self.Ratio, s=self.State1.s)
        self.State3 = self.air.set(P=self.State2.P * self.PressureRatio, v=self.State2.v)
        self.State4 = self.air.set(P=self.State3.P, v=self.State3.v * self.Cutoff)
        self.State5 = self.air.set(v=self.State1.v, s=self.State4.s)

        self.W_Compression = self.State2.u - self.State1.u
        self.W_Power = (self.State4.u - self.State5.u) + self.State3.P * (self.State4.v - self.State3.v)
        self.Q_In = (self.State3.u - self.State2.u) + (self.State4.h - self.State3.h)
        self.Q_Out = self.State5.u - self.State1.u

        self.W_Cycle = self.W_Power - self.W_Compression
        self.Eff = self.W_Cycle / self.Q_In

        self.upperCurve = StateDataForPlotting()
        self.lowerCurve = StateDataForPlotting()
        self.calculated = False
        self.cycleType = 'dual'

    def getSI(self):
        return self.units.SI


class dualCycleController():
    def calc(self):
        print("dual calc called")
    def __init__(self, model=None, ax=None):
        self.model = dualCycleModel() if model is None else model
        self.view = dualCycleView()
        self.view.ax = ax

    # region Functions that operate on the model
    def calc(self):
        T0  = float(self.view.le_TLow.text())
        P0  = float(self.view.le_P0.text())
        V0  = float(self.view.le_V0.text())
        CR  = float(self.view.le_CR.text())
        rp  = float(self.view.le_PressureRatio.text())
        rc  = float(self.view.le_Cutoff.text())
        metric = self.view.rdo_Metric.isChecked()
        self.set(T_0=T0, P_0=P0, V_0=V0, pressure_ratio=rp, cutoff=rc, ratio=CR, SI=metric)

    def set(self, T_0=300.0, P_0=1E5, V_0=3E-3, pressure_ratio=1.5, cutoff=1.2, ratio=18.0, SI=True):
        self.model.units.set(SI=SI)
        self.model.T_initial     = T_0 if SI else T_0 / self.model.units.CF_T
        self.model.p_initial     = P_0 if SI else P_0 / self.model.units.CF_P
        self.model.V_Cylinder    = V_0 if SI else V_0 / self.model.units.CF_V
        self.model.Ratio         = ratio
        self.model.PressureRatio = pressure_ratio
        self.model.Cutoff        = cutoff

        self.model.State1 = self.model.air.set(P=self.model.p_initial, T=self.model.T_initial, name='State 1 - BDC')
        self.model.State2 = self.model.air.set(v=self.model.State1.v / self.model.Ratio, s=self.model.State1.s, name='State 2 - TDC')
        self.model.State3 = self.model.air.set(P=self.model.State2.P * self.model.PressureRatio, v=self.model.State2.v, name='State 3 - const V heat add end')
        self.model.State4 = self.model.air.set(P=self.model.State3.P, v=self.model.State3.v * self.model.Cutoff, name='State 4 - const P heat add end')
        self.model.State5 = self.model.air.set(v=self.model.State1.v, s=self.model.State4.s, name='State 5 - BDC')

        self.model.air.n = self.model.V_Cylinder / self.model.air.State.v
        self.model.air.m = self.model.air.n * self.model.air.MW

        self.model.W_Compression = self.model.State2.u - self.model.State1.u
        self.model.W_Power       = (self.model.State4.u - self.model.State5.u) + self.model.State3.P * (self.model.State4.v - self.model.State3.v)
        self.model.Q_In          = (self.model.State3.u - self.model.State2.u) + (self.model.State4.h - self.model.State3.h)
        self.model.Q_Out         = self.model.State5.u - self.model.State1.u

        self.model.W_Cycle = self.model.W_Power - self.model.W_Compression
        self.model.Eff     = 100.0 * self.model.W_Cycle / self.model.Q_In
        self.model.calculated = True

        self.buildDataForPlotting()
        self.updateView()

    def buildDataForPlotting(self):
        self.model.upperCurve.clear()
        self.model.lowerCurve.clear()
        a = air()

        # 2->3: constant volume, T from T2->T3
        for T in np.linspace(self.model.State2.T, self.model.State3.T, 30):
            state = a.set(T=T, v=self.model.State2.v)
            self.model.upperCurve.add((state.T, state.P, state.u, state.h, state.s, state.v))

        # 3->4: constant pressure, T from T3->T4
        for T in np.linspace(self.model.State3.T, self.model.State4.T, 30):
            state = a.set(T=T, P=self.model.State3.P)
            self.model.upperCurve.add((state.T, state.P, state.u, state.h, state.s, state.v))

        # 4->5: isentropic expansion
        for v in np.linspace(self.model.State4.v, self.model.State5.v, 30):
            state = a.set(v=v, s=self.model.State4.s)
            self.model.upperCurve.add((state.T, state.P, state.u, state.h, state.s, state.v))

        # 5->1: constant volume heat rejection
        for T in np.linspace(self.model.State5.T, self.model.State1.T, 30):
            state = a.set(T=T, v=self.model.State5.v)
            self.model.upperCurve.add((state.T, state.P, state.u, state.h, state.s, state.v))

        # 1->2: isentropic compression (lower curve)
        for v in np.linspace(self.model.State1.v, self.model.State2.v, 30):
            state = a.set(v=v, s=self.model.State1.s)
            self.model.lowerCurve.add((state.T, state.P, state.u, state.h, state.s, state.v))

    # endregion

    # region Functions that operate on the view
    def setWidgets(self, w=None):
        self.view.setWidgets(w)

    def updateView(self):
        self.view.updateView(self.model)

    def plot_cycle_XY(self, X='s', Y='T', logx=False, logy=False, mass=False, total=False):
        self.view.plot_cycle_XY(self.model, X=X, Y=Y, logx=logx, logy=logy, mass=mass, total=total)
    # endregion


class dualCycleView():
    def __init__(self):
        # widget references set later via setWidgets
        self.le_TLow = None
        self.le_THigh = None
        self.le_P0 = None
        self.le_V0 = None
        self.le_CR = None
        self.le_PressureRatio = None
        self.le_Cutoff = None
        self.rdo_Metric = None
        self.ax = None
        self.canvas = None

        # output widgets
        self.le_T1 = None
        self.le_T2 = None
        self.le_T3 = None
        self.le_T4 = None
        self.le_Efficiency = None
        self.le_PowerStroke = None
        self.le_CompressionStroke = None
        self.le_HeatAdded = None

        self.lbl_THigh = None
        self.lbl_TLow = None
        self.lbl_P0 = None
        self.lbl_V0 = None
        self.lbl_CR = None
        self.lbl_T1Units = None
        self.lbl_T2Units = None
        self.lbl_T3Units = None
        self.lbl_T4Units = None
        self.lbl_PowerStrokeUnits = None
        self.lbl_CompressionStrokeUnits = None
        self.lbl_HeatInUnits = None
        self.cmb_Abcissa = None
        self.cmb_Ordinate = None
        self.chk_LogAbcissa = None
        self.chk_LogOrdinate = None
    def setWidgets(self, w=None):
        """Receives the same widget list as Otto/Diesel views."""
        # w order matches someWidgets in OttoDiesel_app.py
        self.lbl_THigh, self.lbl_TLow, self.lbl_P0, self.lbl_V0, self.lbl_CR = w[0], w[1], w[2], w[3], w[4]
        self.le_THigh, self.le_TLow, self.le_P0, self.le_V0, self.le_CR       = w[5], w[6], w[7], w[8], w[9]
        self.le_T1, self.le_T2, self.le_T3, self.le_T4                         = w[10], w[11], w[12], w[13]
        self.lbl_T1Units, self.lbl_T2Units, self.lbl_T3Units, self.lbl_T4Units = w[14], w[15], w[16], w[17]
        self.le_PowerStroke, self.le_CompressionStroke, self.le_HeatAdded, self.le_Efficiency = w[18], w[19], w[20], w[21]
        self.lbl_PowerStrokeUnits, self.lbl_CompressionStrokeUnits, self.lbl_HeatInUnits      = w[22], w[23], w[24]
        self.rdo_Metric, self.cmb_Abcissa, self.cmb_Ordinate                   = w[25], w[26], w[27]
        self.chk_LogAbcissa, self.chk_LogOrdinate                              = w[28], w[29]
        self.ax     = w[30]
        self.canvas = w[31]

        # Dual cycle reuses le_THigh for pressure ratio input
        self.le_PressureRatio = self.le_THigh
        self.le_Cutoff        = self.le_TLow   # reuse TLow field for cutoff

    def updateView(self, model=None):
        if self.cmb_Abcissa is None:
            return
        abcissa  = self.cmb_Abcissa.currentText()
        ordinate = self.cmb_Ordinate.currentText()
        logx     = self.chk_LogAbcissa.isChecked()
        logy     = self.chk_LogOrdinate.isChecked()
        self.updateDisplayWidgets(Model=model)
        if model.calculated:
            self.plot_cycle_XY(model, X=abcissa, Y=ordinate, logx=logx, logy=logy)

    def convertDataCol(self, cycle, colName, data, mass=False, total=False):
        UC = cycle.units
        n  = cycle.air.n
        MW = cycle.air.MW
        TCF = 1.0 if UC.SI else UC.CF_T
        PCF = 1.0 if UC.SI else UC.CF_P
        hCF = 1.0 if UC.SI else UC.CF_e
        uCF = 1.0 if UC.SI else UC.CF_e
        sCF = 1.0 if UC.SI else UC.CF_s
        vCF = 1.0 if UC.SI else UC.CF_v
        nCF = 1.0 if UC.SI else UC.CF_n
        if mass:
            hCF /= MW; uCF /= MW; sCF /= MW; vCF /= MW
        elif total:
            hCF *= n*nCF; uCF *= n*nCF; sCF *= n*nCF; vCF *= n*nCF
        w = colName.lower()
        if w == 't': return [T*TCF for T in data]
        if w == 'h': return [h*hCF for h in data]
        if w == 'u': return [u*uCF for u in data]
        if w == 's': return [s*sCF for s in data]
        if w == 'v': return [v*vCF for v in data]
        if w == 'p': return [P*PCF for P in data]

    def plot_cycle_XY(self, cycle, X='s', Y='T', logx=False, logy=False, mass=False, total=False):
        if X == Y:
            return
        QTPlotting = True
        if self.ax is None:
            self.ax = plt.subplot()
            QTPlotting = False

        ax = self.ax
        ax.clear()
        ax.set_xscale('log' if logx else 'linear')
        ax.set_yscale('log' if logy else 'linear')

        XdataLC = self.convertDataCol(cycle, colName=X, data=cycle.lowerCurve.getDataCol(X), mass=mass, total=total)
        YdataLC = self.convertDataCol(cycle, colName=Y, data=cycle.lowerCurve.getDataCol(Y), mass=mass, total=total)
        XdataUC = self.convertDataCol(cycle, colName=X, data=cycle.upperCurve.getDataCol(X), mass=mass, total=total)
        YdataUC = self.convertDataCol(cycle, colName=Y, data=cycle.upperCurve.getDataCol(Y), mass=mass, total=total)
        ax.plot(XdataLC, YdataLC, color='k')
        ax.plot(XdataUC, YdataUC, color='b')

        cycle.units.setPlotUnits(SI=cycle.units.SI, mass=mass, total=total)
        ax.set_ylabel(cycle.lowerCurve.getAxisLabel(Y, Units=cycle.units), fontsize='large')
        ax.set_xlabel(cycle.lowerCurve.getAxisLabel(X, Units=cycle.units), fontsize='large')
        ax.set_title('Dual Cycle', fontsize='large')
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize='large')

        # plot state circles (5 states)
        for state_orig in [cycle.State1, cycle.State2, cycle.State3, cycle.State4, cycle.State5]:
            s = dc(state_orig)
            s.ConvertStateData(SI=cycle.getSI(), Units=cycle.units, n=cycle.air.n, MW=cycle.air.MW, mass=mass, total=total)
            ax.plot(s.getVal(X), s.getVal(Y), marker='o', markerfacecolor='w', markeredgecolor='k')

        if not QTPlotting:
            plt.show()
        else:
            self.canvas.draw()

    def updateDisplayWidgets(self, Model=None):
        U  = Model.units
        SI = U.SI

        self.lbl_THigh.setText('Press. Ratio (rp):')
        self.lbl_TLow.setText('Cutoff (rc):')
        self.lbl_P0.setText('P0 ({})'.format(U.PUnits))
        self.lbl_V0.setText('V0 ({})'.format(U.VUnits))

        self.lbl_T1Units.setText(U.TUnits)
        self.lbl_T2Units.setText(U.TUnits)
        self.lbl_T3Units.setText(U.TUnits)
        self.lbl_T4Units.setText(U.TUnits)

        if U.changed or Model.calculated:
            if Model.calculated:
                CFE = 1.0 if SI else U.CF_E
                CFP = 1.0 if SI else U.CF_P
                CFV = 1.0 if SI else U.CF_V

                self.le_THigh.setText('{:0.3f}'.format(Model.PressureRatio))
                self.le_TLow.setText('{:0.3f}'.format(Model.Cutoff))
                self.le_P0.setText('{:0.2f}'.format(Model.p_initial * CFP))
                self.le_V0.setText('{:0.4f}'.format(Model.V_Cylinder * CFV))

                self.le_T1.setText('{:0.2f}'.format(Model.State1.T if SI else U.T_KtoR(Model.State1.T)))
                self.le_T2.setText('{:0.2f}'.format(Model.State2.T if SI else U.T_KtoR(Model.State2.T)))
                self.le_T3.setText('{:0.2f}'.format(Model.State3.T if SI else U.T_KtoR(Model.State3.T)))
                self.le_T4.setText('{:0.2f}'.format(Model.State4.T if SI else U.T_KtoR(Model.State4.T)))

                self.le_Efficiency.setText('{:0.3f}'.format(Model.Eff))
                self.le_PowerStroke.setText('{:0.3f}'.format(Model.air.n * Model.W_Power * CFE))
                self.le_CompressionStroke.setText('{:0.3f}'.format(Model.air.n * Model.W_Compression * CFE))
                self.le_HeatAdded.setText('{:0.3f}'.format(Model.air.n * Model.Q_In * CFE))
                self.lbl_PowerStrokeUnits.setText(U.EUnits)
                self.lbl_CompressionStrokeUnits.setText(U.EUnits)
                self.lbl_HeatInUnits.setText(U.EUnits)
            else:
                CFP = 1/U.CF_P if SI else U.CF_P
                CFV = 1/U.CF_V if SI else U.CF_V
                p_initial = float(self.le_P0.text())
                v_initial = float(self.le_V0.text())
                self.le_THigh.setText('1.5')   # default rp
                self.le_TLow.setText('1.2')    # default rc
                self.le_P0.setText('{:0.2f}'.format(p_initial * CFP))
                self.le_V0.setText('{:0.4f}'.format(v_initial * CFV))
            U.changed = False
#endregion


def main():
    dcc = dualCycleController()
    dcc.set(T_0=300.0, P_0=1E5, V_0=3E-3, pressure_ratio=1.5, cutoff=1.2, ratio=18.0, SI=True)
    dcc.plot_cycle_XY(X='v', Y='P', total=True)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main()
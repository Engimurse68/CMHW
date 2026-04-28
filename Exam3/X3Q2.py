"""
Polymer Simulation - CLI
Final Exam Question Deuce

Requires Polymer.py (polymerClasses.py) in the same directory.
Updates to macroMolecule:
  - N drawn from normal distribution (mean=N_target, std=0.1*N_target)
  - PDI calculated as Mw/Mn
"""

#region imports
import math
import random as rnd
import numpy as np
from copy import deepcopy as dc
from Polymer import Position, molecule, macroMolecule
#endregion

# =============================================================================
# UPDATED macroMolecule subclass with normal distribution N and PDI
# =============================================================================
class polyMolecule(macroMolecule):
    def __init__(self, targetN=1000, segmentLength=0.154E-9, merWt=14):
        """
        Extends macroMolecule to draw N from N(targetN, 0.1*targetN).
        """
        # Draw actual N from normal distribution
        actual_N = int(max(1, round(np.random.normal(targetN, 0.1 * targetN))))
        super().__init__(degreeOfPolymerization=actual_N,
                         segmentLength=segmentLength,
                         merWt=merWt)
        self.targetN = targetN


# =============================================================================
# SIMULATION FUNCTION
# =============================================================================
def run_simulation(target_N, num_molecules):
    """
    Build num_molecules polyMolecule objects, run freelyJointedChainModel on each,
    and return statistics.
    """
    molecules = []
    for _ in range(num_molecules):
        m = polyMolecule(targetN=target_N)
        m.freelyJointedChainModel()
        molecules.append(m)

    # --- Center of mass (average over all molecules) ---
    avg_com = Position()
    for m in molecules:
        avg_com += m.centerOfMass
    avg_com /= num_molecules

    # Convert to nm (positions stored in meters)
    com_nm = Position(x=avg_com.x * 1e9,
                      y=avg_com.y * 1e9,
                      z=avg_com.z * 1e9)

    # --- End-to-end distance (convert m -> μm) ---
    e2e_list = [m.endToEndDistance * 1e6 for m in molecules]
    avg_e2e  = np.mean(e2e_list)
    std_e2e  = np.std(e2e_list, ddof=1)

    # --- Radius of gyration (convert m -> μm) ---
    rog_list = [m.radiusOfGyration * 1e6 for m in molecules]
    avg_rog  = np.mean(rog_list)
    std_rog  = np.std(rog_list, ddof=1)

    # --- PDI = Mw / Mn ---
    # Mn = number-average molecular weight = sum(MW) / n
    # Mw = weight-average molecular weight = sum(MW^2) / sum(MW)
    mw_list = [m.MW for m in molecules]
    Mn  = np.mean(mw_list)
    Mw  = np.sum(np.array(mw_list)**2) / np.sum(mw_list)
    PDI = Mw / Mn

    return com_nm, avg_e2e, std_e2e, avg_rog, std_rog, PDI


# =============================================================================
# CLI
# =============================================================================
def main():
    # Get inputs with defaults shown in prompt
    n_input = input("Degree of polymerization (1000)?: ").strip()
    target_N = int(n_input) if n_input else 1000

    m_input = input("How many molecules (50)?: ").strip()
    num_mol = int(m_input) if m_input else 50

    print(f"\nMetrics for {num_mol} molecules of degree of polymerization = {target_N}")

    com, avg_e2e, std_e2e, avg_rog, std_rog, PDI = run_simulation(target_N, num_mol)

    print(f"Avg. Center of Mass (nm) = {com.x:.3f}, {com.y:.3f}, {com.z:.3f}")
    print(f"End-to-end distance (\u03bcm):")
    print(f"  Average   = {avg_e2e:.3f}")
    print(f"  Std. Dev. = {std_e2e:.3f}")
    print(f"Radius of gyration (\u03bcm):")
    print(f"  Average   = {avg_rog:.3f}")
    print(f"  Std. Dev. = {std_rog:.3f}")
    print(f"PDI = {PDI:.2f}")


if __name__ == "__main__":
    main()
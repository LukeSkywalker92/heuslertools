"""
Tools to calculate flux rations between different materials
"""
from periodictable import formula, elements
import math

def ionization_efficiency(Z):
    """
    Calculate the the ionization efficiency for an atom from the atomic number Z
    It is calculated by $$\\frac{\\eta}{\\eta_{N_{2}}}=\\frac{0.4Z}{15}+0.6$$
    """
    return (((0.4*Z)/14)+0.6)

def mol_weight(mat):
    """
    Get the atomic weight for a given chemical formula like `'Sb4'` or `'Mn'`
    """
    return formula(mat).mass

def flux_ratio(meas_x, meas_y):
    """
    Calculate the flux ratio between two `heuslertools.mbe.flux_ratio.FluxMeasurement`s.
    The ratio is calculate with
    $$\\frac{J_X}{J_Y}=\\frac{BEP_X}{BEP_Y}\\cdot\\frac{\\eta_Y}{\\eta_X}\\cdot\\sqrt{\\frac{T_X M_Y}{T_Y M_X}}$$
    """
    return (meas_x.bep/meas_y.bep)*(meas_y.ionization_efficiency/meas_x.ionization_efficiency)*math.sqrt((meas_x.temperature*meas_y.mass)/(meas_y.temperature*meas_x.mass))

class FluxMeasurement(object):

    def __init__(self, form, bep, temperature):
        """
        The FluxMeasurement class represents a flux measurement. It is formed
        by the chemical formula of the material, the beam equivalent pressure
        BEP and the cell temperature
        """
        self.formula = formula(form)
        """Chemical formula like `'Sb4'` or `'Mn'`"""
        self.mass = self.formula.mass
        """Atomic mass of the chemical formula"""
        self.Z = elements.symbol(str(list(self.formula.atoms.keys())[0])).number
        """Atomic number of the atoms in the chemical formula"""
        self.ionization_efficiency = ionization_efficiency(self.Z)
        """ionization efficiency calculated by `heuslertools.mbe.flux_ratio.ionization_efficiency`"""
        self.bep = bep
        """Beam equivalent pressure BEP"""
        self.temperature = temperature + 273.15
        """Temperature of the cell in °C"""

if __name__ == "__main__":
    meas_sb_1 = FluxMeasurement('Sb4', 4e-8, 424.4)
    meas_cu_1 = FluxMeasurement('Cu', 5.5e-9, 996)
    meas_sb = FluxMeasurement('Sb4', 5e-8, 420)
    meas_cu = FluxMeasurement('Cu', 5e-9, 991)
    meas_mn = FluxMeasurement('Mn', 9e-9, 817)

    print('Cu/Mn', flux_ratio(meas_cu, meas_mn))
    print('Mn/Mn', flux_ratio(meas_mn, meas_mn))
    print('Sb/Mn', flux_ratio(meas_sb, meas_mn))
    print()
    print('Sb/Cu 1:', flux_ratio(meas_sb_1, meas_cu_1))
    print('Sb/Cu 2:', flux_ratio(meas_sb, meas_cu))

import math

from periodictable import formula
from scipy.constants import physical_constants

from .si_constants import K_B, MU_BOHR, MU_ZERO, g


class Crystal(object):
    """
    The crystal class allows you to generate a crystal object that allows you
    to perform magnetic unit conversations in context to the crystal.
    You can import it with

    ```from heuslertools.magnetism import Crystal```
    """

    def __init__(self, a, n, mu_eff=0, t_cw=0, c=None, chemical_formula=None):
        self.a = a*1e-10
        """Horizontal lattice constant of crystal in angstroms"""
        self.c = 0
        """Vertical lattice constant of crystal in angstroms.
        Leave blank if it is the same as the horizontal lattice constant"""
        self.mu_eff = mu_eff
        """Theoretical effective paramagnetic moment in bohr magnetons"""
        self.t_cw = t_cw
        if c is None:
            self.c = self.a
        else:
            self.c = c*1e-10
        self.n = n
        """Atoms per unit forumla"""
        self.v = self.a*self.a*self.c
        """Volume of unit cell in \(m^{3}\)"""
        self.curie_constant = (
            MU_ZERO*self.n*self.mu_eff*self.mu_eff*MU_BOHR*MU_BOHR)/(3*K_B*self.v)
        self.chemical_formula = formula(chemical_formula)
        #print("Created Crystal with", "a =", self.a, ", c =", self.c, ", v =", self.v , ", n =", n)

    def get_density(self, unit='kg/m3'):
        # kg/m**3
        density = (self.n*self.chemical_formula.mass *
                   physical_constants['atomic mass constant'][0])/self.v
        if unit == 'kg/m3':
            return density
        elif unit == 'g/cm3':
            return density*1e-3

    def pm_suszeptibility(self, temperature):
        """
        Calculate the theoretical paramagnetic suszeptibility at a given temperature
        """
        return(self.curie_constant/(temperature-self.t_cw))

    def get_exp_eff_moment(self, c):
        """
        Calculate the effective paramagnetic moment for a given Curie constant
        """
        return math.sqrt((c*3*K_B*self.v)/(MU_ZERO*self.n*MU_BOHR*MU_BOHR))

    def get_exp_eff_moment_from_sus(self, slope):
        """
        Calculate the effective paramagnetic moment in bohr magnetons for
        a given slope of the inverse suszeptibility
        """
        return math.sqrt((3*K_B*self.v)/(MU_ZERO*self.n*MU_BOHR*MU_BOHR*slope))

    def mu_eff_to_m_sat(self, mu_eff):
        """
        Calculate the saturation magnetization in bohr magnetons for
        a given effective paramagnetic moment in bohr magnetons
        """
        return 0.5*g*((math.sqrt((g*g)+(4*mu_eff*mu_eff))/(g))-1)

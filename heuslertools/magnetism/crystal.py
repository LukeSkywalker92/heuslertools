import math

MU_BOHR = 9.274009994e-24
K_B = 1.3806e-23
MU_ZERO = 1.2566e-6
g = 2


class Crystal(object):

    def __init__(self, a, n, mu_eff, t_cw, c=None):
        self.a = a*1e-10
        self.mu_eff = mu_eff
        self.t_cw = t_cw
        if c is None:
            self.c = self.a
        else:
            self.c = c*1e-10
        self.n = n
        self.v = self.a*self.a*self.c
        self.curie_constant = (MU_ZERO*self.n*self.mu_eff*self.mu_eff*MU_BOHR*MU_BOHR)/(3*K_B*self.v)
        print("Created Crystal with", "a =", self.a, ", c =", self.c, ", v =", self.v , ", n =", n)

    def pm_suszeptibility(self, temperature):
        return(self.curie_constant/(temperature-self.t_cw))

    def get_exp_eff_moment(self, c):
        return math.sqrt((c*3*K_B*self.v)/(MU_ZERO*self.n*MU_BOHR*MU_BOHR))

    def get_exp_eff_moment_from_sus(self, slope):
        return math.sqrt((3*K_B*self.v)/(MU_ZERO*self.n*MU_BOHR*MU_BOHR*slope))

    def mu_eff_to_m_sat(self, mu_eff):
        return 0.5*g*((math.sqrt((g*g)+(4*mu_eff*mu_eff))/(g))-1)

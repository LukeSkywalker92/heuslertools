import numpy as np
import sympy
import mpmath
from heuslertools.magnetism.si_constants import g, MU_BOHR, K_B

def csch(x):
    return 1 / np.sinh(x)

def brillouin_function(alpha, J):
    a = (2*J+1)/(2*J)
    return a * mpmath.coth(a*alpha) - (1/(2*J) * mpmath.coth(alpha/(2*J)))

def brillouin_first_derivative(y, S):
    return (1/(4*S)) * (csch(y/2)**2 - ((2*S+1)**2)*(csch((2*S+1)*(y/2))**2))


def brillouin_first_derivative_taylor(y, S):
    return ((S+1)/3)-(((1+3*S+4*S*S+2*S*S*S)/30)*(y**2))

def alpha(J, B, T):
    return (g*J*MU_BOHR*B)/(K_B*T)


if __name__ == "__main__":
    


    import matplotlib.pyplot as plt
    plt.figure()
    x = np.linspace(0.00001, 4, 1000)
    y = [brillouin_function(i, alpha(2, 1000, 4)) for i in x]
    y2 = [brillouin_first_derivative_taylor(i, alpha(2, 1000, 4)) for i in x]
    #y2 = [brillouin_first_derivative_taylor(i, alpha(4, 1000, 300)) for i in x]
    #plt.plot(x, y)
    plt.plot(x, np.gradient(y, x))
    plt.plot(x, y2)
    plt.figure()
    plt.plot(x, y)
    plt.show()
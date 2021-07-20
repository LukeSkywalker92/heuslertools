from heuslertools.xrd.materials import CuMnSb, GaSb, NiMnSb, InP
from heuslertools.cristallography.poisson_ratio import a_vert


#print(a_vert(GaSb, CuMnSb, 0.3))
rel_err = 0.03/0.3
a = a_vert(InP, NiMnSb, 0.3)
a_max = a+a*((rel_err**2+(0.007/5.926)**2)**0.5y)
a_min = a-a*((rel_err**2+(0.007/5.926)**2)**0.5y)

print(a_min, a, a_max)
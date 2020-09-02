from heuslertools.magnetism import Crystal

CuMnSb = Crystal(a=6.09, n=4, chemical_formula='CuMnSb')

print(CuMnSb.get_density(unit='kg/m3'), 'kg/m3')
print(CuMnSb.get_density(unit='g/cm3'), 'g/cm3')
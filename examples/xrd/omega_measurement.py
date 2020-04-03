from heuslertools.xrd import OmegaMeasurement
from heuslertools.xrd.materials import CuMnSb
import xrayutilities as xu
import numpy as np
import matplotlib.pyplot as plt

xrd = OmegaMeasurement('data/H1202_omega_fine_002.xrdml')
xrd.print_names()

results, fit = xrd.voigt_fit()

print('FWHM:', round(results[1]*3600, 2), 'arcsec')
print('Max:', int(results[2]))

plt.figure()
plt.semilogy(xrd.data['Omega']-results[0], xrd.data['detector'])
plt.semilogy(xrd.data['Omega']-results[0], fit(xrd.data['Omega']))
plt.show()

from heuslertools.muSR import MUSRMeasurement
import os
import matplotlib.pyplot as plt

m = MUSRMeasurement(os.path.join('data', 'H1300_50GTF_8keV_Tscan_withDiaFrac.dat'))
m.print_names()

print(m.data['eDiaFrac'])

plt.figure()
plt.errorbar(m.data['dataT'], m.data['DiaFrac'], yerr=m.data['eDiaFrac'])
plt.show()
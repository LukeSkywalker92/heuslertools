from heuslertools.muSR import MUSRMeasurement
import os
import matplotlib.pyplot as plt

FILES = [
    'H1300_50GTF_10K_Escan_withDiaFrac.dat',
    'H1300_50GTF_60K_Escan_withDiaFrac.dat',
    'H1300_50GTF_70K_Escan_withDiaFrac.dat'
]

measurements = [MUSRMeasurement(os.path.join('data', f)) for f in FILES]


plt.figure()

for m in measurements:
    plt.errorbar(m.data['dataE'], m.data['DiaFrac'], yerr=m.data['eDiaFrac'], fmt='o', ms=2, capsize=1)


plt.show()
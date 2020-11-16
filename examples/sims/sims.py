from heuslertools.sims import SIMSMeasurement

import matplotlib.pyplot as plt

plt.style.use('heusler')

sims = SIMSMeasurement('data/T4PO_102_H1316PO4.TXT')


plt.semilogy(sims.data['Number'], sims.data['Ru'], label='Ru')
plt.semilogy(sims.data['Number'], sims.data['Mn'], label='Mn')
plt.semilogy(sims.data['Number'], sims.data['Sb'], label='Sb')
plt.semilogy(sims.data['Number'], sims.data['Cu'], label='Cu')
plt.semilogy(sims.data['Number'], sims.data['Ni'], label='Ni')

plt.xlim(0, 3e2)
plt.legend()

plt.axvspan(0, 30, facecolor='b', alpha=0.2)
plt.axvspan(30, 30+68, facecolor='g', alpha=0.2)
plt.axvspan(30+68, 250, facecolor='r', alpha=0.2)

plt.title('H1316 (InP / (InGa)As / 20 nm CuMnSb / 7.5 nm NiMnSb / 5 nm Ru)', fontsize=10)
plt.xlabel('Data Point')
plt.ylabel('Intensity (counts)')

plt.show()
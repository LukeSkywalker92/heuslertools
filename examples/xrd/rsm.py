from heuslertools.xrd import RSMMeasurement
import xrayutilities as xu
import matplotlib.pyplot as plt
import numpy as np


xrd = RSMMeasurement('data/H1202_RSM224_Triple_axis_hi_res.xrdml',
                     material=xu.materials.InAs,
                     geometry='hi_lo',
                     beam_direction=[1, 1, 0],
                     surface_normale=[0, 0, 1],
                     reflex=[2, 2, 4])
#xrd.print_names()
#print(xrd.data['2Theta'])

print(xrd._get_nominal_angle('Omega'))


anggridder = xu.FuzzyGridder2D(300, 300)
anggridder(xrd.data['Omega'], xrd.data['2Theta'], xrd.data['psd'])
angINT = xu.maplog(anggridder.data.transpose(), 3.3, 0)

qgridder, qINT = xrd.get_q_data(size=300, dynamic_range=3.6)
hklgridder, hklINT = xrd.get_hkl_data(size=300, dynamic_range=3.6)


cf = plt.contourf(hklgridder.xaxis, hklgridder.yaxis, hklINT, 100, cmap='jet', extend='min')
cf.cmap.set_under('w')
cb = plt.colorbar(cf)
plt.show()
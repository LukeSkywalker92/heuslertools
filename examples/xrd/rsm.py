from heuslertools.xrd import RSMMeasurement
import xrayutilities as xu
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm

xrd = RSMMeasurement('data/H1202_RSM224_Triple_axis_hi_res.xrdml',
                     material=xu.materials.InAs,
                     geometry='hi_lo',
                     beam_direction=[1, 1, 0],
                     surface_normale=[0, 0, 1],
                     reflex=[2, 2, 4])

qgridder, qINT = xrd.get_q_data(size=300, dynamic_range=3.6)
hklgridder, hklINT = xrd.get_hkl_data(size=300, dynamic_range=3.6)

cf = plt.contourf(hklgridder.xaxis, hklgridder.yaxis, hklINT, 100, cmap='jet', extend='min')
cf.cmap.set_under('w')
cb = plt.colorbar(cf)
plt.show()
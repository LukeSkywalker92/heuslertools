from heuslertools.xrd import RSMMeasurement
from heuslertools.xrd.materials import GaSb, InAs
import xrayutilities as xu
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm



H1202 = RSMMeasurement('data/H1202_RSM224_Triple_axis_hi_res.xrdml',
                     material=InAs,
                     geometry='hi_lo',
                     beam_direction=[1, 1, 0],
                     surface_normale=[0, 0, 1],
                     reflex=[2, 2, 4])



H1232 = RSMMeasurement('data/H1232_rsm224_Pixel_Detector.xrdml',
                     material=GaSb,
                     geometry='hi_lo',
                     beam_direction=[1, 1, 0],
                     surface_normale=[0, 0, 1],
                     reflex=[2, 2, 4])

H1202_hklgridder, H1202_hklINT, H1202_ticks = H1202.get_hkl_data(size=300, dynamic_range=3.6)
H1232_hklgridder, H1232_hklINT, H1232_ticks = H1232.get_hkl_data(size=300, dynamic_range=4.2)

plt.figure()
plt.subplot(121)

cf = plt.contourf(H1202_hklgridder.xaxis, H1202_hklgridder.yaxis, H1202_hklINT, 100, cmap='jet', extend='min')
cf.cmap.set_under('w')
cb = plt.colorbar(cf, ticks = H1202_ticks, format='$10^{%x}$')
cb.set_label(r"Intensity (cps)")
plt.xlabel(r'HH0')
plt.ylabel(r'00L')


plt.xlim(1.99, 2.01)
plt.ylim(3.92, 4.02)

plt.subplot(122)

cf = plt.contourf(H1232_hklgridder.xaxis, H1232_hklgridder.yaxis, H1232_hklINT, 100, cmap='jet', extend='min')
cf.cmap.set_under('w')
cb = plt.colorbar(cf, ticks = H1232_ticks, format='$10^{%x}$')
cb.set_label(r"Intensity (cps)")
plt.xlabel(r'HH0')
plt.ylabel(r'00L')

plt.xlim(1.99, 2.01)
plt.ylim(3.94, 4.04)

plt.tight_layout()
plt.show()
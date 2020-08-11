import os
from matplotlib import ticker
from heuslertools.afm import AFMMeasurement
from heuslertools.plotting.mpl_helpers import set_size
import matplotlib.pylab as plt

fig = plt.figure(figsize=set_size(20, ratio=0.4, cm=True))
afm = AFMMeasurement('data/H1202_1x1um.txt', size=(1e-6, 1e-6))
x0, y0 = 286.284, 130.674 # These are in _pixel_ coordinates!!
x1, y1 = 218.908, 220.332
ax1 = plt.subplot(121)
cf1 = plt.contourf(afm.x, afm.y, afm.z, 100, cmap='afmhot', vmax=12)
profile, line = afm.profile((x0, y0), (x1, y1), linewidth=10)


plt.plot(line[0], line[1], 'k-')
plt.xlabel(r'[1-10]')
plt.ylabel(r'[110]')
cb = plt.colorbar(cf1)
afm.afm_xy_ticks(ax1)
afm.afm_z_ticks(cb, [0, 3, 6, 9, 12, 15])
cb.set_label(r"Height (A)")


afm.afm_aspect_ratio(ax1)
afm.show_scale_bar(ax1, 2.5e-7, r'0.25 µm', (0.2, 0.2), lw=1.5, color='black', fontsize=8)

ax2 = plt.subplot(122)
plt.plot(profile[0]*1e9, profile[1], '-')
plt.hlines(6.65, 50, 150)
plt.hlines(3.33, 50, 150)
plt.annotate(s='', xy=(125,6.65), xytext=(125,3.33), arrowprops=dict(arrowstyle='<->', linewidth=0.6))
plt.text(130, 5.7,'3.3 \AA',
     horizontalalignment='left',
     verticalalignment='center')
plt.hlines(6.6, 260, 360)
plt.hlines(3.81, 260, 360)
plt.annotate(s='', xy=(290,6.6), xytext=(290,3.81), arrowprops=dict(arrowstyle='<->', linewidth=0.6))
plt.text(285, 4.4,'2.8 \AA',
     horizontalalignment='right',
     verticalalignment='center')
plt.xlabel("Length (nm)")
plt.ylabel("Height (\AA)")
plt.xlim(0,375)
plt.ylim(3, 7)
plt.yticks([3, 4, 5, 6, 7])

plt.tight_layout()
plt.show()

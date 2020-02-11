import os
from matplotlib import ticker
from heuslertools.afm import AFMMeasurement
import matplotlib.pylab as plt

fig = plt.figure()
ax0 = plt.gca()
afm = AFMMeasurement(os.path.join('data', 'H1202_1x1um.txt'))

print(afm.rms_roughness())

profile = afm.profile((237, 164), (267, 126), linewidth=20)

cf = plt.contourf(afm.x, afm.y, afm.z, 100, cmap='afmhot')
for c in cf.collections:
    c.set_rasterized(True)
plt.xlabel(r'1 µm')
plt.ylabel(r'1 µm')
cb = plt.colorbar(cf)
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelbottom=False,
    labelleft=False)
tick_locator = ticker.FixedLocator([0, 3, 6, 9])
cb.locator = tick_locator
cb.update_ticks()
cb.set_label(r"Height (\AA)")
plt.plot([237, 267], [164, 126], 'k-', linewidth=20, alpha=0.5)
#ax0.set_aspect('equal')
xleft, xright = ax0.get_xlim()
ybottom, ytop = ax0.get_ylim()
ax0.set_aspect(abs((xright-xleft)/(ybottom-ytop))*1)

plt.figure()
plt.plot(profile)

plt.show()

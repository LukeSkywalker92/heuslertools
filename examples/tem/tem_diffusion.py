from heuslertools.tem import TEMImage
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter, periodogram, find_peaks
import numpy as np
from uncertainties import ufloat

tem = TEMImage('data/pic_013_1.ser')

# get profile
x0, y0 = 520, 633 # These are in _pixel_ coordinates!!
x1, y1 = 527, 960
profile, line = tem.profile((x0, y0), (x1, y1), linewidth=15)

# interpolate + smooth
xx = np.linspace(profile[0].min(),profile[0].max(), 1000)
itp = interp1d(profile[0],profile[1], kind='linear')
window_size, poly_order = 121, 7
yy_sg = savgol_filter(itp(xx), window_size, poly_order)

# find peaks and calculate ru distance
peaks, _ = find_peaks(yy_sg, prominence=50)
diffs = np.diff(xx[peaks])
diff = np.mean(diffs)
ru_distance = ufloat(np.mean(diffs), np.std(diffs))

print('Ru distance:', str(ru_distance))




fig = plt.figure()
ax0 = plt.subplot(121)

#cf = plt.contourf(tem.data['xAxis'], tem.data['yAxis'], tem.data['data'], 20, cmap='Greys_r')
ax0.imshow(tem.z, cmap='Greys_r', origin='lower',aspect='equal')
ax0.plot(line[0], line[1], 'k-')
ax0.set_xlim(470, 570)
ax0.set_ylim(630, 970)


tem.set_xy_ticks(ax0)

tem.show_scale_bar(ax0, 2e-9, r'2 nm', (0.1, 0.1), lw=1.5, color='white', fontsize=10, text_y_offset=0.025)

ax0.set_xlabel('[110]')
ax0.set_ylabel('[001]')

ax1 = plt.subplot(122)
ax1.set_title('Ru distance: ' + str(ru_distance))

ax1.plot(profile[0], profile[1], '-', label='Profile', alpha=0.5)
ax1.plot(xx, yy_sg, '-', label='Smoothed data')
#ax1.plot(xx[peaks], yy_sg[peaks], 'x', label='found Peaks')

plt.legend()
plt.tight_layout()


plt.show()
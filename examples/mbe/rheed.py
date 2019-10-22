import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from spectrum import Periodogram, FourierSpectrum

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

X, Y = np.loadtxt("H1285_sps_intensities.csv", delimiter=',', unpack=True)
X_2, Y_2 = np.loadtxt("d2_intensities.csv", delimiter=',', unpack=True)

Y_s = smooth(Y, 10)

plt.subplot(211)
plt.plot(X, Y/max(Y), '-', ms=1, lw=1)
plt.plot(X, Y_s/max(Y), '-', ms=1, lw=1)
plt.xlabel('Time (s)')
plt.xlim(0, 2000)
plt.ylabel('Intensity (a.u.)')

plt.subplot(212)

p = Periodogram(Y, sampling=0.5)
p.run()
p.plot()

p_2 = Periodogram(Y_s, sampling=0.5)
p_2.run()
p_2.plot()




plt.tight_layout()

plt.show()

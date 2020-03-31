from heuslertools.squid import SQUIDMeasurement
import matplotlib.pyplot as plt
import numpy as np

FILEPATH_SAMPLE = 'data/H1258_CSH_HipII110_[L]_45,7mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_12062019.rso.dat'
X = "Temperature_K"
Y = "Long_Moment_emu"
Y2 = "Long_Scan_Std_Dev"


meas = SQUIDMeasurement(FILEPATH_SAMPLE)
meas.print_names()

x = np.linspace(meas.data[X].min(), meas.data[X].max(), 1000)
y = meas.interpolation(X, Y)


plt.figure()
plt.subplot(211)
plt.plot(meas.data[X], meas.data[Y], 'o')
plt.plot(x, y(x))
plt.xlabel(meas.get_axis_label(X))
plt.ylabel(meas.get_axis_label(Y))
plt.subplot(212)
plt.plot(meas.data[X], meas.data[Y2])
plt.xlabel(meas.get_axis_label(X))
plt.ylabel(meas.get_axis_label(Y2))
plt.tight_layout()
plt.show()

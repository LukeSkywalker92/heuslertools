from heuslertools.squid import SQUIDMeasurement
import matplotlib.pyplot as plt
import numpy as np

FILEPATH_SAMPLE = 'data/H1258_CSH_HipII110_[L]_45,7mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_12062019.rso.dat'
X = "Temperature_K"
Y = "Long_Moment_emu"
Y2 = "Long_Scan_Std_Dev"


meas = SQUIDMeasurement(FILEPATH_SAMPLE)

meas.save('test.dat')

new_meas = SQUIDMeasurement('test.dat')

print(new_meas.filter_data('Temperature_K', '50<x<70', filter_type='delete'))

new_meas.plot(X, Y, 'o')
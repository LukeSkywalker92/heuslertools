import matplotlib.pyplot as plt
from heuslertools.transport import TransportMeasurement


x_name = "Temperature_LS332_K"
y_name = "Rxx_Ohm"
meas = TransportMeasurement('data/RT warming_0T (01).dat', '---------')
meas.append_measurement('data/RT warming_0T (02).dat', '---------')
meas.append_measurement('data/RT warming_0T (03).dat', '---------')
meas.print_names()
meas2 = TransportMeasurement('data/RT Warming_7T (01).dat', '---------')
plt.plot(meas.data[x_name], meas.data[y_name], 'k-', label="0 T")
plt.plot(meas2.data[x_name], meas2.data[y_name], 'r-', label="7 T")
plt.xlabel(meas.names[x_name]["short_name"] + ' (' + meas.names[x_name]["unit"] + ')')
plt.ylabel(meas.names[y_name]["short_name"] + ' (' + meas.names[y_name]["unit"] + ')')
plt.legend()
plt.show()

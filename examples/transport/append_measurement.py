import matplotlib.pyplot as plt
from heuslertools.transport.load_transport_data import TransportMeasurement


x_name = "Temperature_LS332_K"
y_name = "Rxx_Ohm"
meas = TransportMeasurement('data/RT warming_0T (01).dat', '---------')
meas.append_measurement('data/RT warming_0T (02).dat', '---------')
meas.append_measurement('data/RT warming_0T (03).dat', '---------')
meas.print_names()
plt.plot(meas.data[x_name], meas.data[y_name], 'k-')
plt.xlabel(meas.names[x_name]["short_name"] + ' (' + meas.names[x_name]["unit"] + ')')
plt.ylabel(meas.names[y_name]["short_name"] + ' (' + meas.names[y_name]["unit"] + ')')
plt.show()

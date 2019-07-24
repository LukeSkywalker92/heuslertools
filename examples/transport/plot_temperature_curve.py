import matplotlib.pyplot as plt
from heuslertools.transport.load_transport_data import TransportMeasurement


x_name = "Temperature_LS332_K"
y_name = "Rxx_Ohm"
meas1 = TransportMeasurement('data/RT warming_0T (01).dat', '---------')
meas2 = TransportMeasurement('data/RT warming_0T (02).dat', '---------')
meas3 = TransportMeasurement('data/RT warming_0T (03).dat', '---------')
meas1.print_names()
plt.plot(meas1.data[x_name], meas1.data[y_name], 'k-')
plt.plot(meas2.data[x_name], meas2.data[y_name], 'k-')
plt.plot(meas3.data[x_name], meas3.data[y_name], 'k-')
plt.xlabel(meas1.names[x_name]["short_name"] + ' (' + meas1.names[x_name]["unit"] + ')')
plt.ylabel(meas1.names[y_name]["short_name"] + ' (' + meas1.names[y_name]["unit"] + ')')
plt.show()

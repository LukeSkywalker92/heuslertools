from heuslertools.transport import TransportMeasurement

meas = TransportMeasurement('data/RH _7T (02).dat', '---------')
meas.add_data_column("DoubleRxx_Ohm", meas.data['Rxx_Ohm']*2)
meas.print_names()
X = "BField_set_Mercury_iPS_T"
Y = "Rxx_Ohm"
meas.plot(X, Y)
meas.plot(X, 'DoubleRxx_Ohm')

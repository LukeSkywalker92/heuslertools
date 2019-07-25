import matplotlib.pyplot as plt
from heuslertools.transport import TransportMeasurement

meas = TransportMeasurement('data/RH _7T (02).dat', '---------')
meas.print_names()
X = "BField_set_Mercury_iPS_T"
Y = "Rxx_Ohm"
meas.plot(X, Y)

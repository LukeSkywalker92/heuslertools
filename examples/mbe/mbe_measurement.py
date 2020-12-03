from heuslertools.mbe import MBEMeasurement
import matplotlib.pyplot as plt


measurement = MBEMeasurement('data/H1345.txt')

measurement.print_names()

plt.plot(measurement.data['MnOP'], measurement.data['MnTemperature'], 'o')
plt.show()

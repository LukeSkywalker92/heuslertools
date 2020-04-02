from heuslertools.squid import SQUIDMeasurement
import numpy as np
import matplotlib.pyplot as plt

measurement = SQUIDMeasurement('data/H1270_Si_HoopII110_hysteresis_4 K_26072019.rso.dat')

measurement.substract_linear_baseline('Field_Oe', 'Long_Moment_emu', 20000, 50000, mean=True)

plt.figure()
plt.subplot(211)
measurement.plot("Field_Oe", "Long_Moment_emu", 'o-', show=False, ms=2)
plt.subplot(212)
measurement.plot("Field_Oe", "Long_Moment_LinearBaselineSubstracted_emu", 'o-', show=False, ms=2)
plt.tight_layout()
plt.show()

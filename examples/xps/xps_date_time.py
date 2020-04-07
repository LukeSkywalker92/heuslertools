import matplotlib.pyplot as plt
from heuslertools.xps.xps_measurement import XPSMeasurement

FILE = 'data/H1306_mg_Nr3_80eV_pass_Ch3_3_3V_28000_29750_5_20int_det_Sb_bare.csv'

xps = XPSMeasurement(FILE, integration_time=100)

xps.plot("E_b", "CH3_cps")

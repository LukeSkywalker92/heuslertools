import matplotlib.pyplot as plt
from heuslertools.xps.xps_measurement import XPSMeasurement

FILE = 'data/H1282_mg_Nr2_80eV_pass_Ch3_3_3V_6000_50250_10_10_survey_bare.csv'

xps = XPSMeasurement(FILE, integration_time=100)

xps.plot("E_b", "CH3_cps")

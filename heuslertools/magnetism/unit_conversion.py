import math

def gauss_to_tesla(gauss):
    return gauss*1e-4

def tesla_to_gauss(tesla):
    return tesla*1e4

def oersted_to_amps_per_meter(oersted):
    return (oersted*1e3)/(4*math.pi)

def amps_per_meter_to_oersted(amps_per_meter):
    return amps_per_meter*1e-3*4*math.pi

def emu_per_cm3_to_amps_per_meter(emu_per_cm3):
    return emu_per_cm3*1e3

def amps_per_meter_to_emu_per_cm3(amps_per_meter):
    return amps_per_meter*13-3

def emu_to_amps_m2(emu):
    return emu*1e-3

def amps_m2_to_emu(amps_per_m2):
    return amps_per_m2*1e3

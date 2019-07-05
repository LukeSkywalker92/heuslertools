"""
Collection of functions for conversion of magnetic units
You can import them for example with

```from heuslertools.magnetism.unit_conversion import gauss_to_tesla```
"""
import math

def gauss_to_tesla(gauss):
    """Converts gauss to tesla"""
    return gauss*1e-4

def tesla_to_gauss(tesla):
    """Converts tesla to gauss"""
    return tesla*1e4

def oersted_to_amps_per_meter(oersted):
    """Converts Oersted to \(\\frac{A}{m}\)"""
    return (oersted*1e3)/(4*math.pi)

def amps_per_meter_to_oersted(amps_per_meter):
    """Converts \(\\frac{A}{m}\) to Oersted"""
    return amps_per_meter*1e-3*4*math.pi

def emu_per_cm3_to_amps_per_meter(emu_per_cm3):
    """Converts \(\\frac{emu}{cm^{3}}\) to \(\\frac{A}{m}\)"""
    return emu_per_cm3*1e3

def amps_per_meter_to_emu_per_cm3(amps_per_meter):
    """Converts \(\\frac{A}{m}\) to \(\\frac{emu}{cm^{3}}\)"""
    return amps_per_meter*1e-3

def emu_to_amps_m2(emu):
    """Converts \(emu\) to \(Am^{2}\)"""
    return emu*1e-3

def amps_m2_to_emu(amps_per_m2):
    """Converts \(Am^{2}\) to  \(emu\)"""
    return amps_per_m2*1e3

import math
from .si_constants import MU_BOHR
from .unit_conversion import emu_to_amps_m2, oersted_to_amps_per_meter, amps_m2_to_emu


class Layer(object):

    def __init__(self, l, w, h, crystal):
        """
        The layer class allows you to generate a layer object that allows you
        to perform magnetic unit conversations in context to the layer.
        You can import it with

        ```from heuslertools.magnetism import Layer```
        """
        self.l = l
        """Lenght of the layer in meters"""
        self.w = w
        """Width of the layer in meters"""
        self.h = h
        """Height of the layer in meters"""
        self.crystal = crystal
        """`heuslertools.magnetism.crystal.Crystal` object that the layer is made off"""
        self.v = self.l*self.w*self.h
        """Volume of the layer in \(m^{3}\)"""
        print("Created Layer with", "l =", self.l, ", w =", self.w, ", h =", self.h, ", v =", self.v)

    def get_unit_cells_in_layer(self):
        """Get the number of unit cells in the layer"""
        return self.v/self.crystal.v

    def emu_to_amp_per_meter(self, emu):
        """Convert \(emu\) to \(\\frac{A}{m}\)"""
        return emu_to_amps_m2(emu) / self.v

    def amp_per_meter_to_susteptibility(self, amp, field):
        """Convert \(\\frac{A}{m}\) to suszeptibility"""
        return ( amp * 4 * math.pi ) / field

    def ampere_per_meter_to_emu(self, am):
        """Convert \(\\frac{A}{m}\) to \(emu\)"""
        return amps_m2_to_emu(am) * self.v

    def mag_per_unitformula(self, mag):
        """Normalize magnetization to magnetization per unit formula"""
        return ( mag * self.crystal.v ) / self.crystal.n

    def total_mag(self, mpuf):
        """Get total magnetization from magnetization per unit formula"""
        return ( mpuf * self.crystal.n ) / self.crystal.v

    def emu_to_mubohr_per_unitformula(self, emu):
        """Convert \(emu\) to \(\\frac{µ_{B}}{u.f.}\)"""
        return self.mag_per_unitformula(self.emu_to_amp_per_meter(emu)) / MU_BOHR

    def mubohr_per_unitformula_to_emu(self, mubohr):
        """Convert \(\\frac{µ_{B}}{u.f.}\) to \(emu\)"""
        return self.ampere_per_meter_to_emu(self.total_mag(mubohr * MU_BOHR))

    def pm_moment(self, temperature, field):
        """Calculate paramagnetic moment for given temperature [K] and field [Oe]"""
        return (self.crystal.pm_suszeptibility(temperature)*field*self.v*1e6)/(4*math.pi)

    def slope_to_c(self, slope, field):
        """Calculate Curie Weiss constant from field [Oe] and slope of inverse suszeptibility"""
        return 4*math.pi/(slope*field*self.v*1e6)

    def emu_to_sus(self, emu, field):
        """Convert \(emu\) with given field [Oe] to suszeptibility"""
        return emu_to_amps_m2(emu)/(oersted_to_amps_per_meter(field) * self.v)

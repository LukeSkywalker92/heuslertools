import math
from .si_constants import MU_BOHR
from .unit_conversion import emu_to_amps_m2, oersted_to_amps_per_meter, amps_m2_to_emu


class Layer(object):

    def __init__(self, l, w, h, crystal):
        self.l = l
        self.w = w
        self.h = h
        self.crystal = crystal
        self.v = self.l*self.w*self.h
        print("Created Layer with", "l =", self.l, ", w =", self.w, ", h =", self.h, ", v =", self.v)

    def get_unit_cells_in_layer(self):
        return self.v/self.crystal.v

    def emu_to_amp_per_meter(self, emu):
        return emu_to_amps_m2(emu) / self.v

    def amp_per_meter_to_susteptibility(self, amp, field):
        return ( amp * 4 * math.pi ) / field

    def ampere_per_meter_to_emu(self, am):
        return amps_m2_to_emu(am) * self.v

    def mag_per_unitformula(self, mag):
        return ( mag * self.crystal.v ) / self.crystal.n

    def total_mag(self, mpuf):
        return ( mpuf * self.crystal.n ) / self.crystal.v

    def emu_to_mubohr_per_unitformula(self, emu):
        return self.mag_per_unitformula(self.emu_to_amp_per_meter(emu)) / MU_BOHR

    def mubohr_per_unitformula_to_emu(self, mubohr):
        return self.ampere_per_meter_to_emu(self.total_mag(mubohr * MU_BOHR))

    def pm_moment(self, temperature, field):
        return (self.crystal.pm_suszeptibility(temperature)*field*self.v*1e6)/(4*math.pi)

    def slope_to_c(self, slope, field):
        return 4*math.pi/(slope*field*self.v*1e6)

    def emu_to_sus(self, emu, field):
        return emu_to_amps_m2(emu)/(oersted_to_amps_per_meter(field) * self.v)

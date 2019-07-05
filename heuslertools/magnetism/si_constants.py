"""
Si constants for magnetic calculations
You can import them with

```from heuslertools.magnetism.si_constants import MU_BOHR, K_B, MU_ZERO, g```
"""
import math


MU_BOHR = 9.274009994e-24
"""Bohr magneton \(µ_{B}\) in \(\\frac{J}{T}\)"""
K_B = 1.3806e-23
"""Boltzmann constant \(k_{B}\) in \(\\frac{J}{K}\)"""
MU_ZERO = 4*math.pi*1e-7
"""Vacuum permeability \(µ_{0}\) in \(\\frac{N}{A^{2}}\)"""
g = 2
"""g-factor"""

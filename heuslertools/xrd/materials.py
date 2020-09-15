"""
Additional Heusler materials for xrayutilities
"""
import numpy
from xrayutilities.materials import (Crystal, CubicAlloy, CubicElasticTensor, SGLattice)
from xrayutilities.materials.heuslerlib import *
from xrayutilities.materials import elements as e
from xrayutilities.materials import InAs, GaAs
from xrayutilities.materials import *

def _check_elements(*elem):
    ret = []
    for el in elem:
        if isinstance(el, str):
            ret.append(getattr(e, el))
        else:
            ret.append(el)
    return ret

def HalfHeuslerCubic216(X, Y, Z, a, biso=[0, 0, 0], occ=[1, 1, 1], cij=None):
    """
    Half Heusler structure with formula XYZ structure;
    space group F-43m (216)

    Parameters
    ----------
    X, Y, Z :   str or Element
        elements
    a :         float
        cubic lattice parameter in Angstroem

    Returns
    -------
    Crystal
        Crystal describing the Heusler material
    """
    x, y, z = _check_elements(X, Y, Z)
    return Crystal('%s%s%s' % (x.basename, y.basename, z.basename),
                   SGLattice(216, a, atoms=[z, y, x],
                             pos=['4a', '4b', '4c'],
                             b=[biso[0], ] + biso,
                             occ=[occ[0], ] + occ), cij)

# doi:10.1016/j.commatsci.2006.01.013
ZnTe = Crystal("ZnTe", SGLattice(216, 6.101, atoms=[e.Zn, e.Te],
                                 pos=['4a', '4c']),
               CubicElasticTensor(82.0, 42.0, 55.0))

# doi:10.1002/pssc.201600182
CuMnSb = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
NiMnSb = HalfHeuslerCubic216('Ni', 'Mn', 'Sb', 5.926, cij=CubicElasticTensor(1.6707e+11, 8.206e+10, 5.327e+10))

def CuMnSb(occ=[1,1,1]):
    """
    Returns a CuMnSb Material
    """
    return HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10), occ=occ)

# class CuMnSb_defect(CubicAlloy):
#     def __init__(self, occ=(1, 1, 1), defect_type=None, defec_amount=0):
#         """
#         This is WIP and should not be used at the moment.
#         """
#         if defect_type is None:
#             CuMnSb_sto = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
#             CuMnSb_def = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
#         elif defect_type is 'Cu_Mn_SWAP':
#             CuMnSb_sto = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
#             CuMnSb_def = HalfHeuslerCubic216('Mn', 'Sb', 'Cu', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
#         super(CuMnSb_defect, self).__init__(CuMnSb_sto, CuMnSb_def, defec_amount)

class InGaAs(CubicAlloy):

    def __init__(self, x):
        """
        In_{1-x} Ga_x As cubic compound
        """
        super(InGaAs, self).__init__(InAs, GaAs, x)

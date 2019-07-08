"""
Additional Heusler materials for xrayutilities
"""
import numpy
from xrayutilities.materials import (Crystal, CubicAlloy, CubicElasticTensor, SGLattice)
from xrayutilities.materials.heuslerlib import *

def _check_elements(*elem):
    ret = []
    for el in elem:
        if isinstance(el, str):
            ret.append(getattr(elements, el))
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

CuMnSb = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))

def CuMnSb(occ=[1,1,1]):
    """
    Returns a CuMnSb Material
    """
    return HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10), occ=occ)

class CuMnSb_defect(CubicAlloy):
    def __init__(self, occ=(1, 1, 1), defect_type=None, defec_amount=0):
        """
        This is WIP and should not be used at the moment.
        """
        if defect_type is None:
            CuMnSb_sto = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
            CuMnSb_def = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
        elif defect_type is 'Cu_Mn_SWAP':
            CuMnSb_sto = HalfHeuslerCubic216('Cu', 'Mn', 'Sb', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
            CuMnSb_def = HalfHeuslerCubic216('Mn', 'Sb', 'Cu', 6.09, cij=CubicElasticTensor(1.056e+11, 8.27e+10, 5.47e+10))
        super(CuMnSb_defect, self).__init__(CuMnSb_sto, CuMnSb_def, defec_amount)

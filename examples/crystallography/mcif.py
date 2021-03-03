import os

import matplotlib.pyplot as plt
import numpy as np
from heuslertools.cristallography import Crystal
from heuslertools.cristallography.mcif_parser import MCIFParser
from heuslertools.cristallography.mcrystal import MCrystal
from heuslertools.plotting import plot_functions
from heuslertools.plotting.mpl_helpers import set_size
from heuslertools.xrd.materials import CuMnSb

cumnsb = Crystal(CuMnSb)
cumnsb.crystal = MCrystal.from_mcif('/home/luke/Coding/python/heuslertools/examples/crystallography/data/mCuMnSb.cif')
print(cumnsb)
x, y, z, c, r = cumnsb.get_3D_lattice(2, 2, 2)


"""
################################# PLOTTING #####################################
"""


fig = plt.figure(figsize=set_size(10, cm=True, ratio=1))
ax = fig.add_subplot(projection='3d')
ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))
ax.view_init(elev=8, azim=18)

ax.scatter(x, y, z, s=r*200, c=c)
ax.set_xlabel(r'[100]')
ax.set_ylabel(r'[010]')
ax.set_zlabel(r'[001]')
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.axis('off')

cumnsb.show_crystal_boarder(ax, 1, 'k', 2)

ax.text(1, 0, 0, "Sb", horizontalalignment='center',
        verticalalignment='center', color='white')
ax.text(1, 0, 0.5, "Mn", horizontalalignment='center',
        verticalalignment='center', color='white')
ax.text(0.75, 0.25, 0.75, "Cu", horizontalalignment='center',
        verticalalignment='center', color='black')


plt.show()

from heuslertools.xrd import O2TSimulation
from heuslertools.xrd.materials import CuMnSb
import xrayutilities as xu
import numpy as np
import matplotlib.pyplot as plt

##### LAYERSTACK #####
sub = xu.simpack.Layer(xu.materials.InAs, np.inf)
lay1 = xu.simpack.Layer(CuMnSb(), 367, relaxation=0.0)
layerstack = xu.simpack.PseudomorphicStack001('CuMnSb on InAs', sub, lay1)

xrd = O2TSimulation(layerstack)

om, int = xrd.simulate_o2t(0, 0, 2, 0.4)


plt.figure()
plt.semilogy(om, int)
plt.show()

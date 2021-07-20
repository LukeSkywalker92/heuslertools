from heuslertools.xrd import O2TSimulation
from heuslertools.xrd.materials import NiMnSb, InP
import xrayutilities as xu
import numpy as np
import matplotlib.pyplot as plt

##### LAYERSTACK #####
sub = xu.simpack.Layer(InP, np.inf)
lay1 = xu.simpack.Layer(NiMnSb, 400, relaxation=0.0)
layerstack = xu.simpack.PseudomorphicStack001('NiMnSb on InP', sub, lay1)
print(layerstack)
xrd = O2TSimulation(layerstack)

om, int = xrd.simulate_o2t(0, 0, 2, 0.4)


plt.figure()
plt.semilogy(om, int)
plt.show()

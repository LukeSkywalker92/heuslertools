from heuslertools.xrd import O2TSimulation
from heuslertools.xrd.materials import NiMnSb
import xrayutilities as xu
import numpy as np
import matplotlib.pyplot as plt

##### LAYERSTACK #####
plt.figure()
sub = xu.simpack.Layer(xu.materials.GaAs, np.inf)
lay1 = xu.simpack.Layer(NiMnSb, 170, relaxation=0.0)
layerstack = xu.simpack.PseudomorphicStack001('NiMnSb on GaAs', sub, lay1)

xrd = O2TSimulation(layerstack)

om, int = xrd.simulate_o2t(0, 0, 4, 2)
plt.semilogy(om*2, int, label='pseudomorphic')


sub = xu.simpack.Layer(xu.materials.GaAs, np.inf)
lay1 = xu.simpack.Layer(NiMnSb, 170, relaxation=1)
layerstack = xu.simpack.LayerStack('NiMnSb on GaAs', sub, lay1)

xrd = O2TSimulation(layerstack)

om, int = xrd.simulate_o2t(0, 0, 4, 2)
plt.semilogy(om*2, int, label='relaxed')
plt.title('GaAs / 17nm NiMnSb 004')
plt.xlim(50, 75)
plt.xlabel('2Theta (°)')
plt.ylabel('Intensity (a.u.)')
plt.legend()
plt.show()

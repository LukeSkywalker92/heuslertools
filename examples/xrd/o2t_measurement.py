from heuslertools.xrd import O2TMeasurement
from heuslertools.xrd.materials import CuMnSb
import xrayutilities as xu
import numpy as np
import matplotlib.pyplot as plt

##### LAYERSTACK #####
sub = xu.simpack.Layer(xu.materials.InAs, np.inf)
lay1 = xu.simpack.Layer(CuMnSb(), 367, relaxation=0.0)
layerstack = xu.simpack.PseudomorphicStack001('CuMnSb on InAs', sub, lay1)

xrd = O2TMeasurement('data/H1202_o2t_fine_002.xrdml', layerstack)
xrd.print_names()

bounds = [{
    'name': 'CuMnSb_c',
    'min': 6.1359,
    'max': 6.1361
    },{
    'name': 'I0',
    'min': 2e6,
    'max': np.inf
    },
]

sim = xrd.simulate_o2t(0, 0, 2, bounds)

print(sim[1].fit_report())

plt.figure()
plt.semilogy(xrd.data['Omega'], xrd.data['detector'])
plt.semilogy(xrd.data['Omega'], sim[0])
plt.show()

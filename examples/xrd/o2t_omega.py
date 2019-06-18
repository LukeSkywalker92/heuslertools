import xrayutilities as xu
from matplotlib.pylab import *
import matplotlib as mpl
from matplotlib import gridspec
from heuslertools.xrd.materials import CuMnSb




##### INPUT ##### H1227_o2t_002.xrdml
DATA_FILE = 'H1202_o2t_fine_002.xrdml'
DATA_FOLDER = 'data'
OFFSET = 0
QZ_RANGE = 0.4
H, K, L = (0, 0, 2)



##### LAYERS #####
sub = xu.simpack.Layer(xu.materials.InAs, inf)
lay1 = xu.simpack.Layer(CuMnSb(occ=[1,1,1]), 367, relaxation=0.0)

##### LAYERSTACK #####
pls = xu.simpack.PseudomorphicStack001('CuMnSb on InAs', sub, lay1)

##### XRAY PARAMETERS #####
en = 'CuKa1'
wavelength = xu.wavelength('CuKa1')
resol = 2e-10  # resolution in qz


qx = sqrt(sub.material.Q(H, K, L)[0]**2 + sub.material.Q(H, K, L)[1]**2)

d = xu.io.XRDMLFile(DATA_FILE, path=DATA_FOLDER)
scan = d.scans[-1]
tt = scan['2Theta'] - OFFSET
ai = (d.scans[-1]['2Theta'] - OFFSET)/2
qz = xu.simpack.get_qz(qx, ai, en)

# simplest kinematical diffraction model
mk = xu.simpack.KinematicalModel(pls, energy=en, resolution_width=resol)

# general 2-beam theory based dynamical diffraction model
thetaMono = arcsin(wavelength/(2 * xu.materials.Ge.planeDistance(2, 2, 0)))
Cmono = cos(2 * thetaMono)
md = xu.simpack.DynamicalModel(pls, resolution_width=resol,background=1, polarization='both', Cmono=Cmono, I0=1000000000)


figure()
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
subplot(gs[0])

semilogy(ai, scan['detector'], 'o', label='data')
# Dynamic Fit
fitmdyn = xu.simpack.FitModel(md)
fitmdyn.set_param_hint(pls[0].material.name+'_a', vary=True)
fitmdyn.set_param_hint('resolution_width', vary=True)
fitmdyn.set_param_hint('I0', min=2e6)

for l in pls[1:]:
    name = l.material.name.replace('(', '_').replace(')', '_').replace('.', '_')
    fitmdyn.set_param_hint(name+'_c', vary=True)
    fitmdyn.set_param_hint(name+'_a', expr=pls[0].material.name+'_a')
    fitmdyn.set_param_hint(name+'_thickness', vary=True)
fitmdyn.set_param_hint('CuMnSb_c', min=6.1359, max = 6.1361)
fitmdyn.set_param_hint('CuMnSb_thickness', min=365, max = 370)
paramsdyn = fitmdyn.make_params()


fitmdyn.lmodel.set_hkl((H, K, L))
fitr = fitmdyn.fit(d.scans[-1]['detector'], paramsdyn, ai)
print(fitr.fit_report())
simdyn = fitmdyn.eval(fitr.params, x=tt/2)
semilogy(ai, simdyn, label='full dynamical sim')


#legend()
xlim(13.5, 15.5)
ax = gca()
text(0.01, 0.99,'(a)',
     horizontalalignment='left',
     verticalalignment='top',
     transform = ax.transAxes)

xticks([14, 14.5, 15])
xlabel(r'$\mathrm{\omega - 2\theta}$ (°)')
ylabel('Intensity')
tight_layout()



##### INPUT ##### H1227_o2t_002.xrdml
DATA_FILE = 'H1202_omega_fine_002.xrdml'
DATA_FOLDER = 'data'
OFFSET = 0
QZ_RANGE = 0.4
H, K, L = (0, 0, 2)




d = xu.io.XRDMLFile(DATA_FILE, path=DATA_FOLDER)
scan = d.scans[-1]
om = scan['Omega']*3600

fit_params, sd_params, itlim, fitfunc = xu.math.fit.peak_fit(om, scan['detector'], peaktype='PseudoVoigt', plot=False, func_out=True)

OM = (om - fit_params[0])

fit_params, sd_params, itlim, fitfunc = xu.math.fit.peak_fit(OM, scan['detector'], peaktype='PseudoVoigt', plot=False, func_out=True)

print('FWHM:', fit_params[1])
print('Max:', fit_params[2])

subplot(gs[1])

semilogy(OM, scan['detector'], 'o', label='Data')
semilogy(OM, fitfunc(OM), '-', label='Voigt Fit')


tick_params(labeltop=False, labelright=True, labelleft=False)

#legend()
ax = gca()
ax.yaxis.set_label_position("right")
text(0.01, 0.99,'(b)',
     horizontalalignment='left',
     verticalalignment='top',
     transform = ax.transAxes)

xlim(-50, 50)
xticks([-40, 0, 40])
ylim(1, 1e4)
xlabel(r'$\mathrm{\omega}$ (arcsec)')
ylabel('Intensity')
tight_layout()
subplots_adjust(wspace=0)
show()

import matplotlib.pyplot as plt
import numpy as np
from heuslertools.magnetism import Crystal, Layer

if __name__ == "__main__":
    CuMnSb = Crystal(a=6.09, n=4, mu_eff=5.4, t_cw=-160)
    sample = Layer(l=4.5e-3, w=3.5e-3, h=80e-9, crystal=CuMnSb)
    print('')
    print('µ_bohr per unit formula:', sample.emu_to_mubohr_per_unitformula(6e-6))
    print('needed moment in emu:', sample.mubohr_per_unitformula_to_emu(4))

    t1 = np.arange(50.0, 300.0, 1)
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.plot(t1, sample.pm_moment(t1, 50), '-')
    plt.title('1 kOe')
    plt.ylabel('Moment (emu)')
    plt.xlabel('Temperature (K)')
    plt.subplot(1,2,2)
    plt.plot(t1, sample.pm_moment(t1, 10000), '-')
    plt.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    plt.title('10 kOe')
    plt.ylabel('Moment (emu)')
    plt.xlabel('Temperature (K)')
    plt.show()

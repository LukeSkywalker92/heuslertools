from heuslertools.tem import TEMImage
import matplotlib.pyplot as plt
import numpy as np
from heuslertools.xrd.materials import CuMnSb
from heuslertools.cristallography import Crystal


c = Crystal(CuMnSb())


strain = [
    [0.01, 0, 0],
    [0, 0.01, 0],
    [0, 0, 0.16]
]

c.xuCrystal.ApplyStrain(strain)


x, y, c, r = c.get_2D_lattice(4,4,4, [[1,1,0], [0,0,1]], units=True)


tem = TEMImage('data/pic_012_1.ser')
fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111)
ax.imshow(tem.z, cmap='Greys_r', origin='lower', aspect='equal', vmin=tem.z.min(), vmax=tem.z.max())
tem.set_xy_ticks(ax)
tem.show_auto_scale_bar(ax, (0.1, 0.1), color='white', lw=2, fontsize=12, text_y_offset=0.025)

ax.scatter(((x)/tem.pixel_size_x)+700.624, ((y)/tem.pixel_size_y)+560.042, s=r*10, c=c)

plt.tight_layout()

plt.show()
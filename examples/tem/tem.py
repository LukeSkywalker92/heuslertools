from heuslertools.tem import TEMImage
import matplotlib.pyplot as plt

tem = TEMImage('data/pic_013_1.ser')

fig = plt.figure()
ax = plt.gca()

#cf = plt.contourf(tem.data['xAxis'], tem.data['yAxis'], tem.data['data'], 20, cmap='Greys_r')
plt.imshow(tem.z, cmap='Greys_r', origin='lower',aspect='equal')


tem.set_xy_ticks(ax)

tem.show_scale_bar(ax, 2e-9, r'2 nm', (0.1, 0.1), lw=1.5, color='white', fontsize=10, text_y_offset=0.025)

plt.xlabel('[110]')
plt.ylabel('[001]')

plt.show()
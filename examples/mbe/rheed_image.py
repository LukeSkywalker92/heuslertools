from heuslertools.mbe.rheed import RHEEDimage
import matplotlib.pyplot as plt
import numpy as np

hdr_image = RHEEDimage('data/H1300_1-10_07-08-56_hdr.tif')
normal_image = RHEEDimage('data/H1300_1-10_07-08-56.tif')
hdr_image.crop((200, 500, 1000, 900))
normal_image.crop((200, 500, 1000, 900))

plt.subplot(221)
plt.imshow(hdr_image.image)
plt.subplot(223)
plt.plot(hdr_image.profile((0, 50), (800, 50), linewidth=5))
plt.plot(hdr_image.profile((0, 250), (800, 250), linewidth=5))
plt.plot(hdr_image.profile((0, 300), (800, 300), linewidth=5))

plt.subplot(222)
plt.imshow(normal_image.image)
plt.subplot(224)
plt.plot(normal_image.profile((0, 50), (800, 50), linewidth=20))
plt.plot(normal_image.profile((0, 250), (800, 250), linewidth=20))
plt.plot(normal_image.profile((0, 300), (800, 300), linewidth=20))

plt.show()

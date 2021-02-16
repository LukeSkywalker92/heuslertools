from heuslertools.rbs import RBSMeasurement
import matplotlib.pyplot as plt

rbs_random = RBSMeasurement('data/H1202_random.txt')
rbs_channel = RBSMeasurement('data/H1202ch.txt')

plt.figure()

plt.subplot(211)
plt.title('H1202 RBS')
plt.plot(rbs_random.data['D1_Channel_Channel'],
         rbs_random.data['D1_Intensity_Counts'], label='random')
plt.plot(rbs_channel.data['D1_Channel_Channel'],
         rbs_channel.data['D1_Intensity_Counts'], label='channel')
plt.xlabel(rbs_random.get_axis_label('D1_Channel_Channel'))
plt.ylabel(rbs_random.get_axis_label('D1_Intensity_Counts'))
plt.legend()

plt.subplot(212)
plt.title('H1202 PIXE')
plt.semilogy(rbs_random.data['D2_Channel_Channel'],
             rbs_random.data['D2_Intensity_Counts'], label='random')
plt.semilogy(rbs_channel.data['D2_Channel_Channel'],
             rbs_channel.data['D2_Intensity_Counts'], label='channel')
plt.xlabel(rbs_random.get_axis_label('D2_Channel_Channel'))
plt.ylabel(rbs_random.get_axis_label('D2_Intensity_Counts'))
plt.legend()

plt.tight_layout()
plt.show()

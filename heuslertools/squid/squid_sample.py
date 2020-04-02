from heuslertools.squid import gamma
from heuslertools.squid.csh import calculate_beta


class SQUIDSample(object):

    def __init__(self, length, width, weight):
        self.length = length
        self.width = width
        self.weight = weight
        self.area = self._area()
        self.gamma = self._gamma()

    def _area(self):
        return self.length * self.width

    def _gamma(self):
        return gamma(self.length, self.width)

    def beta(self, gap_sample, reference_sample):
        return calculate_beta(gap_sample.weight, reference_sample.weight, self.weight,
                              gap_sample.gamma, reference_sample.gamma, self.gamma)

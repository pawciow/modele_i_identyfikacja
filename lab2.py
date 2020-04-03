import numpy as np
import matplotlib.pyplot as plot
import math

import lab1


# http://pawel.wachel.staff.iiar.pwr.wroc.pl/ModelowanieLab2.pdf


class ThirdLabFirsFunc(lab1.SecondFunction):

    def __init__(self, input_length):
        self.input_length = input_length
        self.sigma = 0.4
        self.mu = 0.0
        self.y_approx = np.random.normal(0, self.sigma, input_length)
        self.x_approx = np.zeros(shape=(1, input_length))
        self.y = np.zeros(self.input_length)
        self.x = np.arange(self.min_x, self.max_x,
                           (self.max_x - self.min_x) / self.input_length)

    def plot_approx(self):
        count, bins, ignored = plot.hist(self.y_approx, 30, density=True)
        plot.plot(bins, 1 / (self.sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - self.mu) ** 2 / (2 * self.sigma ** 2)),
                  linewidth=2, color='r')
        plot.show()


a = ThirdLabFirsFunc(1000)
a.plot_approx()
a.generate()
a.plot_figure()
a.plot_histogram()

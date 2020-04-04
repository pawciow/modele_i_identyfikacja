import numpy as np
import matplotlib.pyplot as plot
import math

import lab1
import lab0


# http://pawel.wachel.staff.iiar.pwr.wroc.pl/ModelowanieLab2.pdf


class ThirdLabFirsFunc(lab1.SecondFunction):

    def __init__(self, input_length):
        super().__init__(input_length)
        self.y_after_rejection = np.zeros(1)
        self.x_after_rejection = np.zeros(1)
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
                  linewidth=2, color='r', label='Funkcja aproksymująca')
        # count, bins, ignored = plot.hist(self.y, 30, density=True)
        plot.plot(self.x, self.y, color='y', label='Funkcja podstawowa')
        # count, bins, ignored = plot.hist(self.y)

        plot.show()

    def reject_points(self):
        for i in range(len(self.y)):
            if self.y[i] > self.y_approx[i]:
                self.y_after_rejection = np.append(self.y_after_rejection, self.y[i])
                self.x_after_rejection = np.append(self.x_after_rejection, self.x[i])

    def plot_histogram(self):
        fig = plot.figure()
        ax = plot.subplot(111)
        ax.hist(self.y_after_rejection, 30, density=True, label='Punkty po odrzuceniu')
        ax.hist(self.y, 30, density=True, label='Punkty przed odrzuceniem')
        ax.legend()
        plot.show()

a = ThirdLabFirsFunc(10000)
# a.provide_x(lab0.provide_sawtooth_generator(10000))
a.generate()
a.plot_approx()
a.reject_points()
# a.plot_figure()
a.plot_histogram()



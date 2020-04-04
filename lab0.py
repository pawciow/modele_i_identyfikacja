import numpy as np
import matplotlib.pyplot as plt


class BaseMethod:
    _name = ''
    input_length = 100000  #set it as default
    y = np.zeros(input_length)
    x = np.zeros(input_length)

    def save_figure(self):
        plt.plot(self.y)
        print("Save figure as {}".format(self._name))
        plt.savefig(self._name)

    def save_histogram(self):
        plt.hist(self.y, bins='auto')
        print("Save figure as {}".format(self._name))
        plt.savefig(self._name)

    def generate(self):
        raise NotImplementedError()

    def plot_figure(self):
        plt.plot(self.y, 'ro')
        plt.show()

    def plot_histogram(self):
        plt.hist(self.y, bins='auto')
        plt.show()


# 1.1
class SawToothGenerator(BaseMethod):
    _tooth_count = 0

    def __init__(self, name, input_length, tooth_count, start_val):
        self._name = name
        self.input_length = input_length
        self.y = np.zeros(input_length)
        self.y[0] = start_val
        self._tooth_count = tooth_count

    def generate(self):
        for i in range(self.input_length-1):
            self.y[i + 1] = \
                self._tooth_count * self.y[i] - np.floor(self._tooth_count * self.y[i])


def provide_sawtooth_generator(n):
    a = SawToothGenerator(input_length=n, tooth_count=13, start_val=0.123456789123456789, name="")
    a.generate()
    return a.y
#
n = 1000
x0 = 0.13123

# ex_one_one = SawToothGenerator("Zadanie1_1_Pilozebny", n, 6, x0)
# ex_one_one.generate()
# ex_one_one.plot_figure()
# ex_one_one.plot_histogram()
# # ex_one_one.save_figure()
# #
# # ex_one_one.plot_figure()
# # ex_one_one.save_figure()


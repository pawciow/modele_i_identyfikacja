import numpy as np
import math
import matplotlib.pyplot as plt

class Model:
    def __init__(self, response_length, a, b):
        self.y = np.zeros(response_length)
        self.x = np.linspace(0,1,response_length)
        self.v = np.zeros(response_length)
        self.N = response_length
        self.e = np.zeros(response_length)

        self.a = a
        self.b = b

    def calculate_impulse_response(self):
        for i in range(self.N):
            if i == 0:
                u = 1
            else:
                u = 0
            self.v[i] = self.V(u, i)
            self.y[i] = self.Y(i)

    def V(self, u, i):
        if (i - 1) < 0:
            return self.b * u
        else:
            return self.b * u + self.a * self.v[i-1]

    def addNoise(self):
        self.e = np.random

    def Y(self, n):
        return self.v[n] + self.e[n]

    def plot_response(self, my_label):
        my_label += '(a={}, b={})'.format(self.a, self.b)
        plt.plot(self.x, self.y, label=my_label)
    #
    # def
    # def mnk(self):
    #     for i in range(self.N - 1):
    #         o = np.append([self.u[i+i], self.y[i]])
    #     # retun approx



a = Model(response_length=10, a=0.5, b=2)
a.calculate_impulse_response()
a.plot_response('Odpowiedź impulsowa')
a.mnk()
# a = Model(response_length=10, a=-0.3, b=3)
# a.calculate_impulse_response()
# a.plot_response('Odpowiedź impulsowa')
# plt.legend()
# plt.show()

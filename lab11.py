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
        # self.e = np.random.uniform(0, 1, self.N)
        self.a = a
        self.b = b

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

    def calculate_response(self, U):
        self.U = U
        for i in range(self.N):
            self.v[i] = self.V(U[i], i)
            self.y[i] = self.Y(i)

    def mnk(self):
        L = 1000 # from task nr. 5
        sum_error = np.array([0, 0], dtype=float)# from task nr. 5
        params = np.array([self.a, self.b])

        for i in range(L):
            self.e = np.random.uniform(0, 1, self.N)
            self.Phi = np.vstack( (self.U[1:], self.y[:-1]) ).T

            self.tmp_z = self.e[1:] - self.e[:-1].dot(self.a) 
            self.tmp_y = self.Phi @ params + self.tmp_z

            approx = np.linalg.inv(self.Phi.T @ self.Phi) @ self.Phi.T @ self.tmp_y
            sum_error += (approx - params)**2
            # print('A = {}, B = {}'.format(self.a, self.b))
            print(approx)
            # plt.plot(L, sum_error[1]/L)
            # print(sum_error[0]/L)
        # print(sum_error)
        print(sum_error/L)

        # plt.show()

        # retun approx

    def instrumental_variables(self):
        self.psi = np.vstack( (self.U[1:], self.v[:-1]) ).T
        self.Phi = np.vstack( (self.U[1:], self.y[:-1]) ).T

        estimation = np.linalg.inv( self.psi.T @ self.Phi ) @ self.psi.T @ self.y[:-1]
        print(estimation)

samples = 10000
singal = np.random.uniform(0, 1, samples)
a = Model(response_length=samples, a=0.5, b=2)
a.calculate_response(singal)
a.mnk()
# a.instrumental_variables()
# a.plot_response('Odpowiedź impulsowa')
# a.mnk()
# plt.hist(a.U, label='Histogram wejścia U_n')
# plt.legend()
# plt.show()
# plt.hist(a.y, label='Histogram wyjścia Y_n')
# plt.legend()
# plt.show()
# plt.hist(a.e, label='Histogram szumu Z')
# plt.legend()
# plt.show()
# plt.scatter(a.U, a.y, label='Wyjście Y_n')
# plt.legend()
# plt.show()
#
# plt.plot(a.v, label='Wykres niezaszumionego V')
# plt.legend()
# plt.show()
# plt.hist(a.v, label='Histogram niezaszumionego V')
# plt.legend()
# plt.show()
import numpy as np
import math
import matplotlib.pyplot as plt


class FirstFunction:
    def __init__(self, n):
        self.n = n
        self.x = np.random.randint(low=-2, high=2, size=n)
        self.y = np.zeros(n)
        self.a = 2
        mu, sigma = 0, 0.1
        self.z = np.random.normal(mu, sigma, n)

    def m(self, x):
        return math.atan(self.a * x)

    def generate(self):
        for i in range(self.n):
            self.y[i] = self.m(self.x[i]) + self.z[i]

    def plot_all(self):
        plt.scatter(self.x, self.y)
        print(self.x)
        print(self.y)
        plt.show()


length = 10000


def first_task(n):
    tmp = FirstFunction(n)
    tmp.generate()
    tmp.plot_all()


first_task(length)

import numpy as np
import matplotlib.pyplot as plot


class Lab3:
    def __init__(self, length, y_normal):
        self.length = length
        self.first_est = np.zeros(length)
        self.second_est = np.zeros(length)
        self.third_est = np.zeros(length)
        self.y = y_normal

    def first_esteem(self, n):
        tmp_sum = 0.0
        for i in range(n):
            tmp_sum += self.y[i]
        return tmp_sum/n

    def second_esteem(self, n):
        tmp_sum = 0
        for i in range(n):
            tmp_sum += pow((self.y[i] - self.first_est[i]), 2)
        return tmp_sum/n

    def third_esteem(self, n):
        tmp_sum = 0
        for i in range(n):
            tmp_sum += pow((self.y[i] - self.first_est[i]), 2)
        if(n -1) == 0:
            return tmp_sum
        return tmp_sum/(n-1)

    def calculate_first_esteem(self):
        for i in range(self.length):
            self.first_est[i] = self.first_esteem(i+1)

    def calculate_second_esteem(self):
        self.calculate_first_esteem()
        for i in range(self.length):
            self.second_est[i] = self.second_esteem(i+1)

    def calculate_third_esteem(self):
        self.calculate_first_esteem()
        for i in range(self.length):
            self.third_est[i] = self.third_esteem(i+1)


def first(n, y):
    a = Lab3(n, y)
    a.calculate_first_esteem()
    plot.title = "Pierwszy estymator"
    plot.plot(a.first_est)
    plot.show()

def demo(n, y_normal):
    plot.plot(y_normal)
    plot.title = "Baza"
    plot.show()
    first(n, y_normal)
    second(n, y_normal)
    third(n, y_normal)

def second(n, y):
    a = Lab3(n, y)
    a.calculate_second_esteem()
    plot.title = "Drugi estymator"
    plot.plot(a.second_est)
    plot.show()

def third(n, y):
    a = Lab3(n, y)
    a.calculate_third_esteem()
    plot.title = "Trzeci estymator"
    plot.plot(a.third_est)
    plot.show()
mu, sigma = 0, 0.1 # mean and standard deviation
len = 1000
demo(len, np.random.normal(mu, sigma,len))
demo(len, np.random.standard_cauchy(len))

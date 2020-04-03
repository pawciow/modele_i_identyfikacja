import numpy as np
import matplotlib.pyplot as plt
import math

from lab0 import BaseMethod, SawToothGenerator, provide_sawtooth_generator


class FirstBaseFunction(BaseMethod):
    max_x = 2
    min_x = -1

    def generate(self):
        for i in range(self.input_length):
            self.y[i] = self._function(self.x[i])

    def __init__(self, input_length):
        self.input_length = input_length
        self.y = np.zeros(self.input_length)
        self.x = np.arange(self.min_x, self.max_x,
                           (self.max_x - self.min_x) / self.input_length)

    def _function(self, x):
        if 0 <= x <= 1:
            return 2 * x
        return 0

    def provide_x(self, x):
        self.x = x

    def plot_figure(self):
        plt.plot(self.x, self.y)
        plt.show()

    def plot_histogram(self):
        plt.hist(self.y)
        plt.show()


class FirstFunctionDistribution(FirstBaseFunction):

    def _function(self, x):
        if 0 <= x <= 1:
            return math.sqrt(x)
        return 0


def excercise_one(n):
    tmp = FirstBaseFunction(n)
    # tmp.x = provide_sawtooth_generator(n)
    tmp.generate()
    tmp.plot_figure()
    tmp.plot_histogram()
    tmp = FirstFunctionDistribution(n)
    # tmp.x = provide_sawtooth_generator(n)
    tmp.generate()
    tmp.plot_figure()
    tmp.plot_histogram()


class SecondFunction(FirstBaseFunction):
    def _function(self, x):
        if -1 < x < 0:
            return x + 1
        if 0 <= x < 1:
            return -x + 1
        return 0


class SecondFunctionDistribution(FirstBaseFunction):
    def _function(self, x):
        if -1 > x:
            return 0
        if -1 < x < 0:
            return (0.5 * pow(x, 2)) + x + 0.5
        if 0 <= x < 1:
            return (-0.5 * pow(x, 2)) + x + 0.5
        return 1


def exercise_two(n):
    tmp = SecondFunction(n)
    # tmp.x = provide_sawtooth_generator(n)
    tmp.generate()
    tmp.plot_figure()
    tmp.plot_histogram()
    tmp = SecondFunctionDistribution(n)
    # tmp.x = provide_sawtooth_generator(n)
    tmp.generate()
    tmp.plot_figure()
    tmp.plot_histogram()


class ThirdFunction(FirstBaseFunction):
    def _function(self, x):
        if x >= 0:
            return math.exp(-x)
        return 0


class ThirdFunctionDistribution(FirstBaseFunction):
    def _function(self, x):
        if x >= 0:
            return -math.log(x)
        return 0


def excercise_three(n):
    tmp = ThirdFunction(n)
    tmp.generate()
    tmp.plot_figure()
    tmp.plot_histogram()
    tmp = ThirdFunctionDistribution(n)
    tmp.generate()
    tmp.plot_figure()
    tmp.plot_histogram()

def demo(n):
    excercise_one(n)
    exercise_two(n)
    excercise_three(n)


exercise_two(1000)
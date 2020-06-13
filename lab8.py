import numpy as np
import math
import matplotlib.pyplot as plt

# X = np.array([[1, 2, 3], [4, 5, 6]])


def white_noise(samples):
    mean = 0
    std = 1

    return np.random.uniform(mean, std, size=samples)


class Model:
    def __init__(self, number_of_inputs, repeats, max_int):
        self.X = np.random.randint(max_int, size=(number_of_inputs, repeats))
        self.Z = white_noise(number_of_inputs)
        self.a = np.random.randint(max_int, size=repeats)
        self.Y = self.X.dot(self.a) + self.Z

    def estimate_least_squares(self):
        self.a_approx = np.linalg.inv((self.X.T @ self.X)) @ self.X.T @ self.Y
        self.Y_approx = self.X.dot(self.a_approx)

    def plot_all(self):
        plt.plot(self.Y, label='Prawdziwe wyjście')
        plt.plot(self.Y_approx, label='Wyjście aproksymowane')
        plt.legend()
        plt.show()

    def plot_imagesc(self):
        covariance_matrix = np.cov(np.linalg.inv((self.X.T @ self.X)))
        plt.imshow(covariance_matrix, extent=[0, 1, 0, 1])
        plt.show()


a = Model(100, 40, 10)

a.estimate_least_squares()
a.plot_all()
a.plot_imagesc()

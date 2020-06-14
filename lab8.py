import numpy as np
import math
import matplotlib.pyplot as plt

# X = np.array([[1, 2, 3], [4, 5, 6]])

#Project is not pretty, I had to do it quickly
def white_noise(samples):
    mean = 0
    std = 10

    return np.random.normal(mean, std, size=samples)


class Model:
    def __init__(self, number_of_inputs, repeats, max_int):
        self.numb = number_of_inputs
        self.X = np.random.normal(max_int, size=(number_of_inputs, repeats))
        self.Z = white_noise(number_of_inputs)
        # self.a = np.random.randint(max_int, size=repeats)
        self.a = np.array([4,2,2,2])
        self.Y = self.X.dot(self.a) #+ self.Z

        self.L = 1000

    def calculate_error(self):
        error = 0
        for i in range(self.L):
            Y_L = self.Y + white_noise(self.numb)
            a_approx = np.linalg.inv((self.X.T @ self.X)) @ self.X.T @ Y_L
            error += (abs(a_approx - self.a))**2

        error = error/self.L
        print(error)


    def plot_all(self):
        plt.plot(self.Y, label='Prawdziwe wyjście')
        plt.plot(self.Y_approx, label='Wyjście aproksymowane')
        plt.legend()
        plt.show()
    #
    # def plot_white_noise(self):
    #     plt.plot(self.Z, label='Zakłócenia')
    #
    # def plot_imagesc(self):
    #     self.covariance_matrix = np.cov(np.linalg.inv((self.X.T @ self.X)))
    #     plt.imshow(self.covariance_matrix, extent=[0, 1, 0, 1])
    #     plt.show()


a = Model(30, 4, 5)
a.calculate_error()
print((a.a))
# print((a.a_approx))
# a.plot_white_noise()
# a.plot_all()
# a.plot_imagesc()
# print(a.covariance_matrix)


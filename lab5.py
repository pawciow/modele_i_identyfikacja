import numpy as np
import math
import matplotlib.pyplot as plt

# Example
mu, sigma = 1, 1  # mean and standard deviation
tmp_length = 1000


class KernelDensityEstimator:
    def __init__(self, len):
        self._N = len
        self._hn = 1
        self.y = np.random.normal(mu, sigma, size=len)
        self.y_approx = np.zeros(len)
        self.x = np.linspace(0, 10, len)
        # self.kernels = np.zeros(len)

    def _kernel(self, x):
        if -0.5 < x < 0.5:
            return 1
        else:
            return 0

    def calculate(self):
        _kernel_sums = 0

        for N in range(self._N):
            if N == 0:
                continue
            for i in range(N):
                _kernel_sums += self._kernel((self.y[i] - self.y[N]) / self._hn)
            self.y_approx[N] = _kernel_sums / (N * self._hn)


def Example(len):
    s = np.random.normal(mu, sigma, len)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r')
    plt.show()


# Example(500)
kde = KernelDensityEstimator(tmp_length)
kde.calculate()
# plt.hist(kde.y, label='Prawdziwa funkcja')
# plt.show()
plt.plot(kde# define some kernels:
# gaussian kernel
kgauss(x) = 1/sqrt(2π) * exp(-1/2 * x^2)
# boxcar
kbox(x) = abs(x) <= 1 ? 1/2 : 0
# triangular
ktri(x) = abs(x) <= 1 ? 1 - abs(x) : 0

# define the KDE function
D(x, h, xi, K) =
  1/(length(xi) * h) * sum(K.((x .- xi) / h))

# evaluate KDE along the x-axis using comprehensions
dens = [D(xstep, sqrt(2.25), x, K) for xstep in x_d, K in (kgauss, kbox, ktri)]

# visualize the kernels
plot(x_d, dens, label = ["Gaussian", "Box", "Triangular"]).y_approx, label='Aproksymacja')

# plt.legend()
plt.show()

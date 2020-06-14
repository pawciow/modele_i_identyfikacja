import numpy as np
import math
import matplotlib.pyplot as plt

# Example
mu, sigma = 1, 1  # mean and standard deviation
tmp_length = 1000000

import numpy as np
import matplotlib.pyplot as plt


def gaussian(x):
    return np.exp(-x ** 2 / 2) * (1 / (np.sqrt(2 * np.pi)))

def trinagular(x):
    return (1-abs(x)) * abs(x) <= 1

def a(x):
    if abs(x) <= 1:
        return 0.5
    else:
        return 0

X = np.random.normal(mu, sigma, 1000)
# X = np.random.triangular(mu, sigma,10, 1000)
N = len(X)

plt.hist(X)
plt.show()
# Plot all available kernels
X_approx = np.linspace(-1, 7, 100)[:, None]


hist_approx = np.zeros(len(X_approx))

h_ns = [0.001, 0.35, 1, 2, 5]
for h in h_ns:
    for i in range(0, N):
        hist_approx += ((gaussian((X_approx - X[i]) /h )) / N)[:, 0]
    label = 'Parametr h_n = {}'.format(h)
    plt.plot(hist_approx, label=label)
plt.legend()
plt.show()




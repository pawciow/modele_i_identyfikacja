import numpy as np
import matplotlib.pyplot as plt


def random(x0, z, n):  # generacja liczb losowych z rozkładu jednostajnego
    x = np.zeros((n + 1, 1))
    x[0] = x0
    for i in range(n):
        x[i + 1] = z * x[i] - np.floor(z * x[i])
    return x[1:n + 1]


def f1(n):  # generacja liczb losowych z rozkładu trójkątnego (zadanie 1 instrukcja 1)
    u = random(0.12341233124, 13, n)
    return np.sqrt(u)


def f3(n):  # generacja liczn losowych z rozkładu wykładniczego
    u = random(0.12341233124, 13, n)
    return -np.log(u)


n = 100000
x0 = 0.123456789123456789
z = 13
n_bins = 10
x = f3(n)
plt.hist(x, bins='auto')
plt.show()


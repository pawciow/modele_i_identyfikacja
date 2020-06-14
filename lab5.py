import numpy as np
import math
import matplotlib.pyplot as plt

# Example
mu, sigma = 1, 1  # mean and standard deviation
tmp_length = 100

class KernelDensityEstimator:
    def __init__(self, len):
        self._N = len
        self._hn = 10
        self.y = np.random.normal(mu, sigma, size=len)
        self.y_approx = np.zeros(len)
        self.x = np.linspace(0, 10, len)
        self.kernels = np.zeros(len)

    # this is really really bad implementation, but I am short on time
    def _kernel(self, it):
        _left_sum = 0
        _right_sum = 0
        _out_of_bound = 0
        _bound_width = int(self._hn / 2)
        for i in range(_bound_width):
            if (it - i) < 0:
                _out_of_bound += 1
                continue
            else:
                _left_sum += self.y[it - i]

        for i in range(_bound_width):
            if it + i >= self._N:
                _out_of_bound += 1
                continue
            # else:
            _right_sum += self.y[it + i]

        if _bound_width - _out_of_bound == 0:
            return 0
        # return _right_sum / (_bound_width - _out_of_bound)
        return (_left_sum + _right_sum) / (_bound_width - _out_of_bound)

    def _func(self, it):
        _sum = 0
        for i in range(it):
            _sum = _sum + self._kernel(i)
        return _sum / (it * self._hn)

    def calculate(self):
        for i in range(self._N):
            self.y_approx[i] = self._func(i+1)


def Example(len):
    s = np.random.normal(mu, sigma, len)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r')
    plt.show()


#Example(500)
kde = KernelDensityEstimator(tmp_length)
kde.calculate()
plt.hist(kde.y, label='Prawdziwa funkcja')
plt.show()
plt.plot(kde.y_approx, label='Aproksymacja')
plt.show()
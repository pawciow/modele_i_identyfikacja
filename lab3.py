import numpy as np
import matplotlib.pyplot as plot

# This code sucks but i'm too tired to refractor. I don't think anyone will see it

class Lab3:
    def __init__(self, length, y_normal, L):
        self.L = L
        self.length = length
        self.first_est = np.zeros(length)
        self.second_est = np.zeros(length)
        self.third_est = np.zeros(length)
        self.num = int(length/L)
        self.first_est_err = np.zeros(self.num)
        self.second_est_err = np.zeros(self.num)
        self.third_est_err = np.zeros(self.num)
        self.y = y_normal

    def first_esteem(self, n): #Estymator wartości oczekiwanej
        tmp_sum = 0.0
        for i in range(n):
            tmp_sum += self.y[i]
        return tmp_sum / n

    def second_esteem(self, n): #Estymator wariancji
        tmp_sum = 0
        for i in range(n):
            tmp_sum += pow((self.y[i] - self.first_est[i]), 2)
        return tmp_sum / n

    def third_esteem(self, n): #Estymator kowariancji
        tmp_sum = 0
        for i in range(n):
            tmp_sum += pow((self.y[i] - self.first_est[i]), 2)
        if (n - 1) == 0:
            return tmp_sum
        return tmp_sum / (n - 1)

    def calculate_first_esteem(self):
        for i in range(self.length):
            self.first_est[i] = self.first_esteem(i + 1)

    def calculate_second_esteem(self):
        self.calculate_first_esteem()
        for i in range(self.length):
            self.second_est[i] = self.second_esteem(i + 1)

    def calculate_third_esteem(self):
        self.calculate_first_esteem()
        for i in range(self.length):
            self.third_est[i] = self.third_esteem(i + 1)

    def calculate_first_esteem_error(self):
        mean = np.mean(self.y)
        tmp_sum = 0
        number_of_calculations = self.num
        for i in range(number_of_calculations):
            for j in range(self.L):
                tmp_sum += pow(self.first_est[self.L * i + j] - mean, 2)
            self.first_est_err[i] = tmp_sum/self.L
            tmp_sum = 0

    def calculate_second_esteem_error(self):
        mean = np.var(self.y)
        tmp_sum = 0
        number_of_calculations = self.num
        for i in range(number_of_calculations):
            for j in range(self.L):
                tmp_sum += pow(self.second_est[self.L * i + j] - mean, 2)
            self.second_est[i] = tmp_sum/self.L
            tmp_sum = 0

    def calculate_third_esteem_error(self):
        mean = np.var(self.y)
        tmp_sum = 0
        number_of_calculations = self.num
        for i in range(number_of_calculations):
            for j in range(self.L):
                tmp_sum += pow(self.third_est[self.L * i + j] - mean, 2)
            self.third_est_err[i] = tmp_sum/self.L
            tmp_sum = 0



    def subplot__all_for_first_est(self):
        fig, (ax1, ax2) = plot.subplots(2, 1)
        ax1.plot(self.first_est)
        ax2.plot(self.first_est_err)
        ax1.set_title('Estymacja')
        ax2.set_title('Błąd empiryczny')
        plot.show()

    def subplot__all_for_second_est(self):
        fig, (ax1, ax2) = plot.subplots(2, 1)

        ax1.plot(self.second_est)
        ax2.plot(self.second_est_err)
        ax1.set_title('Estymacja')
        ax2.set_title('Błąd empiryczny')
        plot.show()

    def subplot__all_for_third_est(self):
        fig, (ax1, ax2) = plot.subplots(2, 1)

        ax1.plot(self.third_est)
        ax2.plot(self.third_est_err)
        ax1.set_title('Estymacja')
        ax2.set_title('Błąd empiryczny')
        plot.show()



def first(n, y, L):
    a = Lab3(n, y, L)
    a.calculate_first_esteem()
    a.calculate_first_esteem_error()
    a.subplot__all_for_first_est()


def second(n, y, L):
    a = Lab3(n, y, L)
    a.calculate_second_esteem()
    a.calculate_second_esteem_error()
    a.subplot__all_for_second_est()

def third(n, y, L):
    a = Lab3(n, y, L)
    a.calculate_third_esteem()
    a.calculate_third_esteem_error()
    a.subplot__all_for_third_est()


def demo(n, y_normal, L):
    plot.plot(y_normal)
    # plot.show()
    # plot.hist(y_normal, bins='auto')
    plot.show()
    first(n, y_normal, L)
    second(n, y_normal, L)
    third(n, y_normal, L)
    print("END OF CALCULATIONS")


# mu, sigma = 0, 0.1  # mean and standard deviation
mu, sigma = 1, 0.4  # mean and standard deviation
L = 10
length = 1000
demo(length, np.random.normal(mu, sigma, length), L)
# y = np.random.standard_cauchy(length)
# y= y[(y>-25) & (y<25)]  # truncate distribution so it plots well

# demo(len(y), y)
# print(np.var(y))
# print(np.mean(y))


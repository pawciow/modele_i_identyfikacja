import lab1


class FirstFunction(lab1.FirstBaseFunction):
    def __init__(self, input_length):
        super().__init__(input_length)

    def generate_n_rand_nums(self, n):
        self.provide_x(lab1.provide_sawtooth_generator(n))
        self.generate()
        self.subplot_all()
x = FirstFunction(1000)
x.generate_n_rand_nums(1000)
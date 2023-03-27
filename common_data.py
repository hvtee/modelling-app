import numpy


class CommonData:
    common_data = []

    def __init__(self):
        # self.omega: float = 6 * pow(10, 9)
        self.omega = numpy.linspace(6 * pow(10, 9), 6 * pow(10, 10), 540)
        try:
            self.mu_0: float = 4 * 3.14 * pow(10, -7)
            self.epsilon_0 = 8.85 * pow(10, -12)
            self.mu_1 = complex(input("\nmu1(a-bj): "))
            self.mu_2 = complex(input("mu2(a-bj): "))
            self.sigma_1 = int(input("sigma1: "))
            self.sigma_2 = int(input("sigma2: "))
            self.c = float(input("c: "))
            self.a = int(input("a(nm): ")) * pow(10, -9)
            self.d = int(input("d(m): "))
        except ValueError or IOError:
            print("Invalid value!")

        CommonData.common_data.append(self)

    @classmethod
    def create_common_data(cls):
        return cls()

    @classmethod
    def show_common_data(cls):
        counter = 0
        for obj in cls.common_data:
            print("\nCOMMON:")
            print(f"SET No: {counter}")
            print(f"omega: {obj.omega[0]} - {obj.omega[-1]}")
            print(f"mu0: {obj.mu_0}")
            print(f"mu1: {obj.mu_1}")
            print(f"mu2: {obj.mu_2}")
            print(f"c: {obj.c}")
            print(f"a: {obj.a}")
            print(f"d: {obj.d}")
            print(f"sigma1: {obj.sigma_1}")
            print(f"sigma2: {obj.sigma_2}")
            print(f"epsilon0: {obj.epsilon_0}")
            # print(f"epsilon1: {obj.epsilon_1[0]} - {obj.epsilon_1[-1]}")
            # print(f"epsilon2: {obj.epsilon_2[0]} - {obj.epsilon_2[-1]}\n")
            counter += 1

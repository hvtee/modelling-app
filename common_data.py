import os
import pickle

import numpy


class CommonData:
    common_data = []

    def __init__(self):
        try:
            # self.omega: float = 6 * pow(10, 9)
            self.omega = numpy.linspace(6 * pow(10, 9), 6 * pow(10, 10), 540)
            self.mu_0: float = 4 * 3.14 * pow(10, -7)
            self.epsilon_0 = 8.85 * pow(10, -12)
            self.mu_1 = complex(input("\nmu1(a-bj): "))
            self.mu_2 = complex(input("mu2(a-bj): "))
            self.sigma_1 = int(input("sigma1: "))
            self.sigma_2 = int(input("sigma2: "))
            self.c = float(input("c: "))
            self.a = int(input("a(nm): ")) * pow(10, -9)
            self.d = float(input("d(m): "))

            CommonData.common_data.append(self)
        except ValueError or IOError:
            print("Invalid value!")

    @classmethod
    def create_common_data(cls):
        return cls()

    @classmethod
    def show_common_data(cls):
        if len(CommonData.common_data) == 0:
            return print("Common data is empty!")
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
            counter += 1

    @staticmethod
    def save_instances_to_file():
        if not CommonData.common_data:
            print("No instances to save in common_data.pkl.")
            return

        with open("data/common_data.pkl", 'wb') as file:
            pickle.dump(CommonData.common_data, file)
            print("Saved to common_data.pkl successfully")

    @staticmethod
    def load_instances_from_file():
        if not os.path.exists("data/common_data.pkl") or os.path.getsize("data/common_data.pkl") == 0:
            print("common_data.pkl file is empty or does not exist.")
            return

        with open("data/common_data.pkl", 'rb') as file:
            CommonData.common_data = pickle.load(file)

    @staticmethod
    def load_examples_from_file():
        if not os.path.exists("data/examples_common_data.pkl") or os.path.getsize("data/examples_common_data.pkl") == 0:
            print("examples_common_data.pkl file is empty or does not exist.")
            return

        with open("data/examples_common_data.pkl", 'rb') as file:
            CommonData.common_data = pickle.load(file)
            print("examples_common_data.pkl loaded successfully")

import os
import pickle

import numpy


class ImpedanceData:
    impedance_data = []

    def __init__(self):
        # self.omega: float = 6 * pow(10, 9)
        try:
            self.name = input("Name of common data set: ")
            if any(data.name == self.name for data in ImpedanceData.impedance_data):
                raise ValueError("Name already exists")
            self.omega = numpy.linspace(6 * pow(10, 9), 6 * pow(10, 10), 540)
            self.ro = float(input("\nro: "))
            self.C = float(input("C(pF): ")) * pow(10, -12)
            self.L = float(input("L(pHn): ")) * pow(10, -12)

            user_choice = 0
            while user_choice not in ["1", "2", "3", "4"]:
                user_choice = str(input("""Choose impedance:
                1 - consistent
                2 - part_parallel
                3 - consistent_parallel
                4 - parallel
                Input: """))
                print()

                if user_choice == "1":
                    self.Z = self.ro + 1j * (self.omega * self.L - (1 / (self.omega * self.C)))
                    self.Z_type = "consistent"
                elif user_choice == "2":
                    self.Z = (self.ro + 1j * self.omega * self.L) / (1j * self.omega * self.C * (
                            self.ro + 1j * (self.omega * self.L - (1 / (self.omega * self.C)))))
                    self.Z_type = "part_parallel"
                elif user_choice == "3":
                    self.Z = self.ro + (1 / (1j * self.omega * self.C + (1 / (1j * self.omega * self.L))))
                    self.Z_type = "consistent_parallel"
                elif user_choice == "4":
                    self.Z = 1 / (1 / self.ro + 1j * (self.omega * self.C - (1 / (self.omega * self.L))))
                    self.Z_type = "parallel"

            ImpedanceData.impedance_data.append(self)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")

    @classmethod
    def create_impedance_data(cls):
        return cls()

    @classmethod
    def show_impedance_data(cls):
        if len(ImpedanceData.impedance_data) == 0:
            return print("Impedance data is empty!")
        counter = 0
        for obj in cls.impedance_data:
            print("\nIMPEDANCE: ")
            print(f"Set No: {counter}")
            print(f"Name of impedance data set: {obj.name}")
            print(f"ro: {obj.ro}")
            print(f"C: {obj.C}")
            print(f"L: {obj.L}")
            print(f"Z: {obj.Z[0]} - {obj.Z[-1]}, {obj.Z_type}\n")
            counter += 1

    @staticmethod
    def save_instances_to_file():
        if not ImpedanceData.impedance_data:
            print("No instances to save in impedance_data.pkl.")
            return

        with open("data/impedance_data.pkl", 'wb') as file:
            pickle.dump(ImpedanceData.impedance_data, file)
            print("Saved impedance_data.pkl successfully")

    @staticmethod
    def load_instances_from_file():
        if not os.path.exists("data/impedance_data.pkl") or os.path.getsize("data/impedance_data.pkl") == 0:
            print("impedance_data.pkl file is empty or does not exist.")
            return

        with open("data/impedance_data.pkl", 'rb') as file:
            ImpedanceData.impedance_data = pickle.load(file)

    @staticmethod
    def load_examples_from_file():
        if not os.path.exists("data/examples_impedance_data.pkl") or \
               os.path.getsize("data/examples_impedance_data.pkl") == 0:
            print("examples_impedance_data.pkl file is empty or does not exist.")
            return

        with open("data/examples_impedance_data.pkl", 'rb') as file:
            ImpedanceData.impedance_data = pickle.load(file)
            print("examples_impedance_data.pkl loaded successfully")

# Z_from_mu_consistent = ro + 1j * (ImpedanceData.impedance_data * L - (1 / (CommonData.omega * C)))
# Z_from_mu_part_parallel = (ro + 1j * CommonData.omega * L) / (
#         1j * CommonData.omega * C * (ro + 1j * (CommonData.omega * L - (1 / (CommonData.omega * C)))))
# Z_from_mu_consistent_parallel = ro + (1 / (1j * CommonData.omega * C + (1 / (1j * CommonData.omega * L))))
# Z_from_mu_parallel = 1 / (1 / ro + 1j * (CommonData.omega * C - (1 / (CommonData.omega * L))))

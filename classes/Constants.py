import numpy


class Constants:
    mu_0: float = 4 * 3.14 * pow(10, -7)
    epsilon_0: float = 8.85 * pow(10, -12)

    @staticmethod
    def create_frequency():
        try:
            print("Choose frequency in GHz: from 'BEGIN' GHz to 'END' GHz")
            begin = float(input("Input 'BEGIN' GHz: "))
            end = float(input("Input 'END' GHz: "))
            omega = numpy.linspace(begin * pow(10, 9), end * pow(10, 9))
            return omega*2*3.14
        except ValueError or IOError:
            print("Wrong format")

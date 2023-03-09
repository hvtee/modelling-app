import numpy

# omega = numpy.linspace(6 * pow(10, 9), 6 * pow(10, 10), 540)
omega: float = 6 * pow(10, 9)
mu_0: float = 4 * 3.14 * pow(10, -7)
mu_1: complex = 2 - 2j
mu_2: complex = 10 - 2j
c: float = 0.1
a: float = 50 * pow(10, -9)
ro: float = 0.001
C: float = 1 * pow(10, -12)
L: float = 1 * pow(10, -12)

Z_from_mu_consistent = ro + 1j * (omega * L - (1 / (omega * C)))
Z_from_mu_part_parallel = (ro + 1j * omega * L) / (1j * omega * C * (ro + 1j * (omega * L - (1 / (omega * C)))))
Z_from_mu_consistent_parallel = ro + (1 / (1j * omega * C + (1 / (1j * omega * L))))
Z_from_mu_parallel = 1 / (1 / ro + 1j * (omega * C - (1 / (omega * L))))

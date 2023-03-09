import cmath

from input import *

Z = Z_from_mu_part_parallel

Q_mu = (1 / mu_2) - ((1j * omega * a * mu_0) / (2 * Z))
B_mu = ((3 - 5 * c) - mu_1 * Q_mu * (6 - 7 * c)) / (3 - 2 * c)
mu_from_omega = (-B_mu + pow(B_mu * B_mu + 8 * mu_1 * Q_mu, 0.5)) / (4 * Q_mu)
# mu_from_omega = (-B_mu + cmath.sqrt(B_mu * B_mu + 8 * mu_1 * Q_mu)) / (4 * Q_mu)

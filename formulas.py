import math

import numpy
import matplotlib.pyplot as plot
from math import e
from common_data import CommonData
from impedance_data import ImpedanceData


def graph(x, y, str):
    real = y.real
    imaginary = y.imag
    plot.figure()
    plot.plot(x / (2 * 3.14), real, 'r')
    plot.plot(x / (2 * 3.14), imaginary, 'g')
    plot.title(f"{str}(w/2pi)")
    plot.ylabel(str)
    plot.xlabel('w/2pi, Hz')
    plot.grid(True)


def solve(number_cd, number_id):
    omega = CommonData.common_data[number_cd].omega
    mu_0 = CommonData.common_data[number_cd].mu_0
    epsilon_0 = CommonData.common_data[number_cd].epsilon_0
    mu_1 = CommonData.common_data[number_cd].mu_1
    mu_2 = CommonData.common_data[number_cd].mu_2
    sigma_1 = CommonData.common_data[number_cd].sigma_1
    sigma_2 = CommonData.common_data[number_cd].sigma_2
    c = CommonData.common_data[number_cd].c
    a = CommonData.common_data[number_cd].a
    d = CommonData.common_data[number_cd].d
    Z_from_omega = ImpedanceData.impedance_data[number_id].Z

    Q_mu = (1 / mu_2) - ((1j * omega * a * mu_0) / (2 * Z_from_omega))
    B_mu = ((3 - 5 * c) - mu_1 * Q_mu * (6 - 7 * c)) / (3 - 2 * c)
    mu_from_omega = (-B_mu + pow(B_mu * B_mu + 8 * mu_1 * Q_mu, 0.5)) / (4 * Q_mu)

    epsilon_1 = 1 - 1j * (sigma_1 / (omega * epsilon_0))
    epsilon_2 = 2 - 1j * (sigma_2 / (omega * epsilon_0))
    Q_epsilon = (1 * Z_from_omega * omega * a * epsilon_0) / (1j * 2 + Z_from_omega * omega * a * epsilon_0 * epsilon_2)
    B_epsilon = (3 * c - 1 - epsilon_1 * Q_epsilon * (3 * c - 2))
    epsilon_from_omega = (B_epsilon + pow(B_epsilon * B_epsilon + 8 * epsilon_1 * Q_epsilon, 0.5)) / (4 * Q_epsilon)

    mu = mu_0 * mu_from_omega
    epsilon = epsilon_0 * epsilon_from_omega
    Z = pow(mu / epsilon, 0.5)

    gamma = 1j * omega * pow(mu * epsilon, 0.5)
    alpha = 8.68 * gamma.real

    A_0 = 20 * numpy.log10(abs(((Z - 377) / (Z + 377))))
    A_1 = alpha * d
    A_2 = 20 * numpy.log10(abs(pow((377 + Z), 2) / (4 * 377 * Z)))
    A_3 = 20 * numpy.log10(abs(1 + pow(e, (-2 * alpha * d) / 8.69) * pow(((Z - 377) / (Z + 377)), 2)))

    T = A_1 + A_2 + A_3
    D = 1 - pow(10, A_0 / 20) - pow(10, -T / 20)

    graph(omega, mu_from_omega, "mu")
    graph(omega, epsilon_from_omega, "epsilon")
    graph(omega, A_0, "A_0")
    graph(omega, T, "T")
    graph(omega, D, "D")
    plot.show()

import math
from math import log
from common_data import CommonData
from impedance_data import ImpedanceData
import matplotlib.pyplot as plot


def graph(x, y, str):
    real = y.real
    imaginary = y.imag

    plot.plot(x / (2 * 3.14), real, 'r')
    plot.plot(x / (2 * 3.14), imaginary, 'g')
    plot.ylabel(str)
    plot.xlabel('w/2pi, Hz')
    plot.show()


def solve_mu(number_cd, number_id):
    Q_mu = (1 / CommonData.common_data[number_cd].mu_2) - (
            (1j * CommonData.common_data[number_cd].omega * CommonData.common_data[number_cd].a *
             CommonData.common_data[number_cd].mu_0) / (2 * ImpedanceData.impedance_data[number_id].Z))

    B_mu = ((3 - 5 * CommonData.common_data[number_cd].c) - CommonData.common_data[number_cd].mu_1 * Q_mu * (
            6 - 7 * CommonData.common_data[number_cd].c)) / (3 - 2 * CommonData.common_data[number_cd].c)

    mu_from_omega = (-B_mu + pow(B_mu * B_mu + 8 * CommonData.common_data[number_cd].mu_1 * Q_mu, 0.5)) / (4 * Q_mu)

    graph(CommonData.common_data[number_cd].omega, mu_from_omega, "mu")


def solve_epsilon(number_cd, number_id):
    epsilon_1 = 1 - 1j * (CommonData.common_data[number_cd].sigma_1 / (
            CommonData.common_data[number_cd].omega * CommonData.common_data[number_cd].epsilon_0))

    epsilon_2 = 2 - 1j * (CommonData.common_data[number_cd].sigma_2 / (
            CommonData.common_data[number_cd].omega * CommonData.common_data[number_cd].epsilon_0))

    Q_epsilon = (ImpedanceData.impedance_data[number_id].Z * CommonData.common_data[number_cd].omega *
                 CommonData.common_data[number_cd].a * CommonData.common_data[number_cd].epsilon_0) \
                / \
                (1j * 2 + ImpedanceData.impedance_data[number_id].Z * CommonData.common_data[number_cd].omega
                 * CommonData.common_data[number_cd].a * CommonData.common_data[number_cd].epsilon_0
                 * epsilon_2)

    B_epsilon = (3 * CommonData.common_data[number_cd].c - 1 - epsilon_1 * Q_epsilon * (
            3 * CommonData.common_data[number_cd].c - 2))

    epsilon_from_omega = (B_epsilon + pow(
        B_epsilon * B_epsilon + 8 * epsilon_1 * Q_epsilon, 0.5)) / (4 * Q_epsilon)

    graph(CommonData.common_data[number_cd].omega, epsilon_from_omega, "epsilon")


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


    Q_mu = (1 / CommonData.common_data[number_cd].mu_2) - (
            (1j * CommonData.common_data[number_cd].omega * CommonData.common_data[number_cd].a *
             CommonData.common_data[number_cd].mu_0) / (2 * ImpedanceData.impedance_data[number_id].Z))

    B_mu = ((3 - 5 * CommonData.common_data[number_cd].c) - CommonData.common_data[number_cd].mu_1 * Q_mu * (
            6 - 7 * CommonData.common_data[number_cd].c)) / (3 - 2 * CommonData.common_data[number_cd].c)

    mu_from_omega = (-B_mu + pow(B_mu * B_mu + 8 * CommonData.common_data[number_cd].mu_1 * Q_mu, 0.5)) / (4 * Q_mu)

    epsilon_1 = 1 - 1j * (CommonData.common_data[number_cd].sigma_1 / (
            CommonData.common_data[number_cd].omega * CommonData.common_data[number_cd].epsilon_0))

    epsilon_2 = 2 - 1j * (CommonData.common_data[number_cd].sigma_2 / (
            CommonData.common_data[number_cd].omega * CommonData.common_data[number_cd].epsilon_0))

    Q_epsilon = (ImpedanceData.impedance_data[number_id].Z * CommonData.common_data[number_cd].omega *
                 CommonData.common_data[number_cd].a * CommonData.common_data[number_cd].epsilon_0) / \
                (1j * 2 + ImpedanceData.impedance_data[number_id].Z * CommonData.common_data[number_cd].omega
                 * CommonData.common_data[number_cd].a * CommonData.common_data[number_cd].epsilon_0
                 * epsilon_2)

    B_epsilon = (3 * CommonData.common_data[number_cd].c - 1 - epsilon_1 * Q_epsilon * (
            3 * CommonData.common_data[number_cd].c - 2))

    epsilon_from_omega = (B_epsilon + pow(
        B_epsilon * B_epsilon + 8 * epsilon_1 * Q_epsilon, 0.5)) / (4 * Q_epsilon)

    mu = CommonData.common_data[number_cd].mu_0 * mu_from_omega
    epsilon = CommonData.common_data[number_cd].epsilon_0 * epsilon_from_omega
    Z = pow(mu / epsilon, 0.5)

    gamma = 1j * CommonData.common_data[number_cd].omega * pow(mu * epsilon, 0.5)
    alpha = 8.68 * gamma.real

    A_0 = 20 * log(abs((Z - 377) / (Z + 377)))
    A_1 = alpha * CommonData.common_data[number_cd].d
    A_2 = 20 * log(abs((Z * Z + 377) / (Z * 4 * 377)))
    A_3 =20 * log(abs(1+pow(math.e, -2*alpha*d/8.69)))
    T = A_1 + A_2 + A_3

    graph(CommonData.common_data[number_cd].omega, mu_from_omega, "mu")
    graph(CommonData.common_data[number_cd].omega, epsilon_from_omega, "epsilon")

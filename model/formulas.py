import numpy
import matplotlib.pyplot as plot
from math import e
from model.Matrix import Matrix
from model.Constants import Constants
from model.Nanoparticles import Nanoparticles
from model.Fibers import Fibers


def graph(x, y, string):
    real = y.real
    imaginary = y.imag
    plot.figure()
    plot.plot(x / (2 * 3.14), real, 'r')
    plot.plot(x / (2 * 3.14), imaginary, 'g')
    plot.title(f"{string}(\u03C9/2\u03C0)")
    plot.ylabel(string)
    plot.xlabel('\u03C9/2\u03C0, Hz')
    plot.grid(True)


def solve(number_npart, number_nstruct, number_envir, omega, Z):
    mu_0 = Constants.mu_0
    epsilon_0 = Constants.epsilon_0
    mu_1 = Matrix.matrix_data[number_envir].mu_1
    mu_2 = Nanoparticles.nanoparticles_data[number_npart].mu_2
    sigma_1 = Matrix.matrix_data[number_envir].sigma_1
    sigma_2 = Nanoparticles.nanoparticles_data[number_npart].sigma_2
    c = Nanoparticles.nanoparticles_data[number_npart].c
    a = Nanoparticles.nanoparticles_data[number_npart].a
    d = Matrix.matrix_data[number_envir].d
    ro = Fibers.fibers_data[number_nstruct].ro
    C = Fibers.fibers_data[number_nstruct].C
    L = Fibers.fibers_data[number_nstruct].L

    omega_copy = numpy.copy(omega)
    var = {'ro': ro, 'C': C, 'L': L, 'omega': omega_copy}
    Z_from_omega = eval(Z, var)
    # Z_from_omega = complex(eval(Z.format(ro=ro, C=C, L=L, omega=omega_str)))

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

    graph(omega, mu_from_omega, "\u03BC")
    graph(omega, epsilon_from_omega, "\u03B5")
    graph(omega, A_0, "R")
    graph(omega, T, "T")
    graph(omega, D, "D")
    plot.show()

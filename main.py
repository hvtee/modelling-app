from formulas import *
import matplotlib.pyplot as plot
import numpy

# print("omega: ", omega)
# print("mu_0: ", mu_0)
# print("mu_1: ", mu_1)
# print("mu_2: ", mu_2)
# print("a: ", a)
# print("Z: ", Z_from_mu)
# print("Q: ", Q_mu)
# print("B: ", B_mu)
# print("mu_from_omega: ", mu_from_omega)

# plot.plot(omega, mu_from_omega)
# plot.show()
#
# # extract real part
# x = [ele.real for ele in mu_from_omega]
# # extract imaginary part
# y = [ele.imag for ele in mu_from_omega]
#
# # plot the complex numbers
# plot.scatter(x, y)
# plot.ylabel('Imaginary')
# plot.xlabel('Real')
# plot.show()

# extract real part using numpy array
x = mu_from_omega.real
# extract imaginary part using numpy array
y = mu_from_omega.imag

# plot the complex numbers
plot.plot(x, 'r')
plot.plot(y, 'g')
plot.show()
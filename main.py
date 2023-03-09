from formulas import *
import matplotlib.pyplot as plot

print("omega: ", omega)
print("mu_0: ", mu_0)
print("mu_1: ", mu_1)
print("mu_2: ", mu_2)
print("a: ", a)
print("Z: ", Z)
print("Q: ", Q_mu)
print("B: ", B_mu)
print("mu_from_omega: ", mu_from_omega)


# real = mu_from_omega.real
# imag = mu_from_omega.imag
#
# plot.plot(omega / (2 * 3.14), real, 'r')
# plot.plot(omega / (2 * 3.14), imag, 'g')
# plot.ylabel('u')
# plot.xlabel('w/2pi, Hz')
# plot.show()

# plot.plot(omega, mu_from_omega)
# plot.show()
#
# # extract real part
# x = [ele.real for ele in mu_from_omega]
# # extract imaginary part
# y = [ele.imag for ele in mu_from_omega]
# # plot the complex numbers
# plot.scatter(x, y)

# plot.show()

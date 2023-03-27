from threading import Thread
import matplotlib.pyplot as plt
import numpy

# def func1():
#     print('Working')
#
#
# def func2():
#     print("Working")


# Thread(target=func1).start()
# Thread(target=func2).start()

x = numpy.linspace(-10, 10)
y1 = x * x
y2 = x * x * x
y3 = 1 / x

plt.figure()
plt.plot(x, y1)
plt.title('y1 = x * x')
plt.xlabel('x')
plt.ylabel('y1')

# График y2
plt.figure()
plt.plot(x, y2)
plt.title('y2 = x * x * x')
plt.xlabel('x')
plt.ylabel('y2')

# График y3
plt.figure()
plt.plot(x, y3)
plt.title('y3 = 1 / x')
plt.xlabel('x')
plt.ylabel('y3')

plt.show()
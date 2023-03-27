from threading import Thread


def func1():
    print('Working')


def func2():
    print("Working")


Thread(target=func1).start()
Thread(target=func2).start()

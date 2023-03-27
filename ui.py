from functions import *


def show_actions():
    print("""\nActions:
    1 - create common data
    2 - show common data
    3 - create impedance
    4 - show impedance
    5 - run modelling
    6 - exit""")
    print()


def do_action():
    action = str(input("Input action: "))

    if action == "1":
        CommonData.create_common_data()
    elif action == "2":
        CommonData.show_common_data()
    elif action == "3":
        ImpedanceData.create_impedance_data()
    elif action == "4":
        ImpedanceData.show_impedance_data()
    elif action == "5":
        run_model()
    elif action == "6":
        quit()

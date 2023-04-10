from functions import *
import tkinter


def show_actions():
    print("""\nActions:
    1 - Create common data
    2 - Create impedance data
    3 - Show common data  
    4 - Show impedance data
    5 - Run modelling
    6 - Save common data
    7 - Save impedance data
    8 - Load common data
    9 - Load impedance data
    0 - exit""")
    print()


def do_action():
    action = str(input("Input action: "))

    if action == "1":
        CommonData.create_common_data()

    elif action == "2":
        ImpedanceData.create_impedance_data()

    elif action == "3":
        CommonData.show_common_data()

    elif action == "4":
        ImpedanceData.show_impedance_data()

    elif action == "5":
        run_model()

    elif action == "6":
        if len(CommonData.common_data) == 0:
            print("Common data is empty")
            return

        choice = CommonData.common_data[choose_common_data()]
        CommonData.save_to_db(choice)

    elif action == "7":
        if len(ImpedanceData.impedance_data) == 0:
            print("Impedance data is empty")
            return

        choice = ImpedanceData.impedance_data[choose_impedance_data()]
        ImpedanceData.save_to_db(choice)

    elif action == "8":
        CommonData.load_from_db()

    elif action == "9":
        ImpedanceData.load_from_db()

    elif action == "0":
        quit()

# class UI:

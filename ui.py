from functions import *


def show_actions():
    print("""\nActions:
    1 - Create common data
    2 - Create impedance data
    3 - Show common data  
    4 - Show impedance data
    5 - Run modelling
    6 - Save data
    7 - Load data
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
        CommonData.save_instances_to_file()
        ImpedanceData.save_instances_to_file()
    elif action == "7":
        CommonData.load_instances_from_file()
        CommonData.load_instances_from_file()
    elif action == "0":
        quit()

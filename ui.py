from modelling import *
import tkinter


def show_actions():
    print("""\nActions:
    1 - Create nanoparticles data
    2 - Create environment data
    3 - Show nanoparticles data  
    4 - Show nanostructures data
    5 - Show environment data
    6 - Run modelling
    7 - Save nanoparticles data
    8 - Load nanoparticles data
    9 - Save environment data
    10 - Load environment data
    11 - Set frequency
    0 - exit""")
    print()


def do_action():
    action = str(input("Input action: "))

    if action == "1":
        Nanoparticles.create_nanoparticles_data()

    elif action == "2":
        Environment.create_environment_data()

    elif action == "3":
        Nanoparticles.show_nanoparticles_data()

    elif action == "4":
        Nanostructures.show_nanostructures_data()

    elif action == "5":
        Environment.show_environment_data()

    elif action == "6":
        run_model()

    elif action == "7":
        if len(Nanoparticles.nanoparticles_data) == 0:
            print("nanoparticles_data is empty")
            return

        choice = Nanoparticles.nanoparticles_data[choose_nanoparticles_data()]
        Nanoparticles.save_to_db(choice)

    elif action == "8":
        Nanoparticles.load_from_db()

    elif action == "9":
        if len(Environment.environment_data) == 0:
            print("environment_data is empty")
            return

        choice = Environment.environment_data[choose_environment_data()]
        Environment.save_to_db(choice)

    elif action == "10":
        Environment.load_from_db()

    elif action == "11":
        Constants.create_frequency()

    elif action == "0":
        quit()


class UI:
    pass

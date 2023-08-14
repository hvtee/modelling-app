from model.modelling import *


def show_actions():
    print("""\nActions:
    1 - Create nanoparticles data
    2 - Save nanoparticles data
    3 - Load nanoparticles data
    4 - Show nanoparticles data
      
    5 - Create environment data
    6 - Save environment data
    7 - Load environment data
    8 - Show environment data

    9 - Create nanostructures data
    10 - Save nanostructures data
    11 - Load nanostructures data
    12 - Show nanostructures data
   
    13 - Run modelling
    0 - exit""")
    print()


def do_action():
    action = str(input("Input action: "))

    if action == "1":
        Nanoparticles.create_nanoparticles_data()
    elif action == "2":
        if len(Nanoparticles.nanoparticles_data) == 0:
            print("nanoparticles_data is empty")
            return
        choice = Nanoparticles.nanoparticles_data[choose_nanoparticles_data()]
        Nanoparticles.save_to_db(choice)
    elif action == "3":
        Nanoparticles.load_from_db()
    elif action == "4":
        Nanoparticles.show_nanoparticles_data()

    elif action == "5":
        Matrix.create_matrix_data()
    elif action == "6":
        if len(Matrix.matrix_data) == 0:
            print("matrix_data is empty")
            return
        choice = Matrix.matrix_data[choose_matrix_data()]
        Matrix.save_to_db(choice)
    elif action == "7":
        Matrix.load_from_db()
    elif action == "8":
        Matrix.show_matrix_data()

    elif action == "9":
        Fibers.create_fibers_data()
    elif action == "10":
        if len(Fibers.fibers_data) == 0:
            print("fibers_data is empty")
            return
        choice = Fibers.fibers_data[choose_fibers_data()]
        Fibers.save_to_db(choice)
    elif action == "11":
        Fibers.load_from_db()
    elif action == "12":
        Fibers.show_fibers_data()
    elif action == "13":
        run_model()
    elif action == "0":
        quit()


class UI:
    pass

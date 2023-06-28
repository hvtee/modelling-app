from classes import Nanoparticles
from formulas import *


def choose_impedance():
    user_choice = 0
    while user_choice not in ["1", "2", "3", "4"]:
        user_choice = str(input("""Choose impedance:
                   1 - consistent
                   2 - part_parallel
                   3 - consistent_parallel
                   4 - parallel
                   Input: """))
        print()

        if user_choice == "1":
            Z = "ro + 1j * (omega * L - (1 / (omega * C)))"
            # Z = "{ro} + 1j * ({omega} * {L} - (1 / ({omega} * {C})))"
            return Z
        elif user_choice == "2":
            Z = "(ro + 1j * omega * L) / (1j * omega * C * (ro + 1j * (omega * L - (1 / (omega * C)))))"
            # Z = "({ro} + 1j * {omega} * {L}) / (1j*{omega}*{C} * ({ro} + 1j * ({omega} * {L} - (1 / ({omega} * {C})))))"
            return Z
        elif user_choice == "3":
            Z = "ro + (1 / (1j * omega * C + (1 / (1j * omega * L))))"
            # Z = "{ro} + (1 / (1j * {omega} * {C} + (1 / (1j * {omega} * {L}))))"
            return Z
        elif user_choice == "4":
            Z = "1 / (1 / ro + 1j * (omega * C - (1 / (omega * L))))"
            # Z = "1 / (1 / {ro} + 1j * ({omega} * {C} - (1 / ({omega} * {L}))))"
            return Z
        # else:
        #     print("Wrong choice!")
        #     return



def choose_nanoparticles_data():
    Nanoparticles.show_nanoparticles_data()
    return int(input("nanoparticles_data. You choose SET No: "))


def choose_nanostructures_data():
    Nanostructures.show_nanostructures_data()
    return int(input("nanostructures_data.You choose SET No: "))


def choose_environment_data():
    Environment.show_environment_data()
    return int(input("environment_data.You choose SET No: "))


def run_model():
    if len(Nanoparticles.nanoparticles_data) != 0 and len(Nanostructures.nanostructures_data) != 0:
        npart_choice = choose_nanoparticles_data()
        nstruct_choice = choose_nanostructures_data()
        envir_choice = choose_environment_data()

        if npart_choice > len(Nanoparticles.nanoparticles_data) - 1 or npart_choice < 0:
            npart_choice = 0
            print("Invalid nanoparticles_data SET №, common data -> SET №0")
        if nstruct_choice > len(Nanostructures.nanostructures_data) - 1 or nstruct_choice < 0:
            nstruct_choice = 0
            print("Invalid nanostructures_data dataSET №, impedance data -> SET №0")
        if envir_choice > len(Environment.environment_data) - 1 or envir_choice < 0:
            envir_choice = 0
            print("Invalid environment_data SET №, impedance data -> SET №0")

        omega = Constants.create_frequency()
        Z = choose_impedance()
        solve(npart_choice, nstruct_choice, envir_choice, omega, Z)
    else:
        print(" nanoparticles_data or nanostructures_data or environment_data are missing!")
        return

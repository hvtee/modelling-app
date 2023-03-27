import common_data
from formulas import *


def choose_common_data():
    CommonData.show_common_data()
    return int(input("COMMON DATA. You choose SET No: "))


def choose_impedance_data():
    ImpedanceData.show_impedance_data()
    return int(input("IMPEDANCE DATA.You choose SET No: "))


def run_model():
    if len(CommonData.common_data) != 0 and len(ImpedanceData.impedance_data) != 0:
        cd_choice = choose_common_data()
        id_choice = choose_impedance_data()

        if cd_choice > len(CommonData.common_data) - 1 or cd_choice < 0:
            cd_choice = 0
            print("Invalid common data SET №, common data -> SET №0")
        if id_choice > len(ImpedanceData.impedance_data) - 1 or id_choice < 0:
            id_choice = 0
            print("Invalid impedance dataSET №, impedance data -> SET №0")

        # solve_mu(cd_choice, id_choice)
        # solve_epsilon(cd_choice, id_choice)
        solve(cd_choice, id_choice)
    else:
        print("Common data or Impedance data are missing!")

# print_info()
# graph(omega, mu_from_omega)
# graph(omega, epsilon_from_omega)

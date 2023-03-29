from ui import *


def main_loop():
    CommonData.load_examples_from_file()
    ImpedanceData.load_examples_from_file()
    while True:
        show_actions()
        do_action()

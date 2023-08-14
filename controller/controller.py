from view.ui import *


def main_loop():
    Fibers.load_from_db()
    Nanoparticles.load_examples()
    Matrix.load_examples()
    while True:
        show_actions()
        do_action()

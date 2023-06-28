from ui import *


def main_loop():
    Nanostructures.load_from_db()
    Nanoparticles.load_examples()
    Environment.load_examples()
    while True:
        show_actions()
        do_action()

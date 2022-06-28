from modules.animation import load_animation
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--initdb", dets="initdb", help="Setup database")
    options = parser.parse_args()
    return options

options = get_arguments()

def init():
    load_animation()
    print("Ready for work :)")

init(options.initdb)

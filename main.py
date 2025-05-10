"""
@author: Gagan Sopori
"""
from application.controller.MainController import MainController


def main():
    pimoroni = MainController()
    pimoroni.start_clock()


if __name__ == '__main__':
    main()

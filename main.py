"""
@author: Gagan Sopori
"""
from src.services.BuildClockScreen import BuildClockScreen


def main():
    pimoroni = BuildClockScreen()
    pimoroni.start_clock()


if __name__ == '__main__':
    main()

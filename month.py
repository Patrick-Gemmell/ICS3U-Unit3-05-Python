#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: October 2019
# This program finds if a rectangle is a square


def main():
    # this function finds if a rectangle is a square
    while True:
        # input
        month = int(input("Give me a month: "))

        # process and output
        print("your month is")
        if month == 1:
            print("January")
            break
        elif month == 2:
            print("February")
            break
        elif month == 3:
            print("March")
            break
        elif month == 4:
            print("April")
            break
        elif month == 5:
            print("May")
            break
        elif month == 6:
            print("June")
            break
        elif month == 7:
            print("July")
            break
        elif month == 8:
            print("August")
            break
        elif month == 9:
            print("September")
            break
        elif month == 10:
            print("October")
            break
        elif month == 11:
            print("November")
            break
        elif month == 12:
            print("December")
            break
        else:
            print("Error, it is not a number between 1-12")


if __name__ == "__main__":
    main()

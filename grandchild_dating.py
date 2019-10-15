#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program makes the user guess the random number.


def main():
    print("This is a test to see if you are good for my granddaughter.")
    age = input("Enter your age: ")
    try:
        age = int(age)
        if age < 25 or age > 45:
            print("Get out of here!")
        elif int(age) > 25 and int(age) < 45:
            print("You are accepted!")
    except ValueError:
        print("You didn’t follow my instructions!")


if __name__ == "__main__":
    main()

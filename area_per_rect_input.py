#!/usr/bin/env python3
# Created By: Xiaohan
# Date: Feb 21, 2025
# This program calculates the area and perimeter of a rectangle based of user's input


# ask users to input the data for length and width in cm
length = int(input("Please enter the length of the rectangle in cm: "))
width = int(input("Enter the width of the rectangle in cm"))

# based on the data user input, provide the formula applied for calculation
area = length * width
perimeter = 2 * (length + width)


def main():
    # print out the result {} with the following sentences in ""
    print("")
    print("For the rectangle with a dimension of {}cm * {}cm".format(length, width))
    print("the area is {}cm^2".format(area))
    print("the perimeter is {}cm".format(perimeter))


if __name__ == "__main__":
    main()

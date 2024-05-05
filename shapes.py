# Python

import math

# This file will calculate the areas and volumes for some shapes.

def calculate_circle_area(radius):
    area = math.pi * radius * radius
    return area


def main():
    print(f'Circle Area is: {calculate_circle_area(10)}')


main()
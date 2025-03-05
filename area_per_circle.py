#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 5, 2025
# Calculator for the area and circumference of a circle
import math


def main():
    # Get radius from user
    radius = float(input("Enter the radius(cm): "))

    # Calculate Area (πr2)
    area = math.pi * (math.pow(radius, 2))
    # Calculate Circumference (2πr)
    circumference = 2 * math.pi * radius

    # Display Area
    print(f"The area is {area:.2f}cm\u00b2")
    # Display Circumference
    print(f"The circumference is {circumference:.2f}cm")


if __name__ == "__main__":
    main()

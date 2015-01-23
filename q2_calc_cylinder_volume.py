__author__ = 'limenglin'

from math import pi

radius = int(input("Enter a integer as the radius:"))
length = int(input("Enter a integer as the length:"))

volume = radius * radius * pi * length

print("The volume of cylinder is", "{0:.1f}".format(volume))

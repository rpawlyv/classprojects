from math import *

shapes = ["cone", "cube", "tetrahedron", "sphere", "cylinder", "dodecahedron", "reuleaux_triangle"]


class Cone():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surfaceArea(self):
        #you do need a * symbol before parenthesis. Its easy to forget this since human math lets us do that!
        coneSA = pi * self.radius * (self.radius + sqrt(pow(self.height, 2) + pow(self.radius, 2)))
        return coneSA

    def volume(self):
        coneVolume = 1.0 / 3.0 * pi * pow(self.radius, 2) * self.height
        return coneVolume


def main():
    ans = input(
        "This program is used to calculate the surface area and volume of a selected shape; would you like to continue? Y: yes N: no")
    if ans == "N" or ans == "n": quit()
    shape = int(input(
        "Select number corresponding to shape; 1:cone, 2:cube, 3:tetrahedron. 4:sphere, 5:cylinder, 6:dodecahedron, 7:reuleaux triangle"))
    usrRadius = float(input(
        "You are to calculate the surface area and volume of a " + shapes[shape - 1] + ". What is the radius of the " +
        shapes[shape - 1] + "?"))
    usrHeight = float(input("What is the height of the " + shapes[shape - 1]))
    usrCone = Cone(usrRadius, usrHeight)
    print("Your cone's surface area is " + str(usrCone.surfaceArea()))
    print("Your cone's volume is " + str(usrCone.volume()))

main()

class Vehicle:

    def __init__(self, color, doors, tires):
        self._color = color
        self.doors = doors
        self.tires = tires

    def _brake(self):
        print(f'braking a {self._color}')

    def setcolor(self, newColor):
        self._color = newColor

    def getcolor(self):
        return self._color


v1 = Vehicle('red', 4, 4)
v2 = Vehicle('black', 2, 6)

print(v1.getcolor())
v1.setcolor('white')
print(v1.getcolor())
#
# v1.brake()
# v2.brake()
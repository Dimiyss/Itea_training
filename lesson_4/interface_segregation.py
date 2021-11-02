from abc import ABC, abstractmethod


class IShape(ABC):
    @abstractmethod
    def draw(self):
        pass


class ICircle(ABC):
    @abstractmethod
    def drawCircle(self):
        pass


class Circle(ICircle):
    def drawCircle(self):
        print(f'this is circle =)')

    def creator(self):
        pass


class CustomShape(IShape):
    def draw(self):
        pass


c = Circle()

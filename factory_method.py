from abc import ABC, abstractmethod

class AbstractPerson(ABC):

    def __init__(self):
        self.movement = self.choose_side()

    @abstractmethod
    # Factory method
    def choose_side(self):
        """ Side """

    def action(self):
        print(self.movement.move())


class Person1(AbstractPerson):

    def choose_side(self):
        return PersonMoveLeft()

class Person2(AbstractPerson):

    def choose_side(self):
        return PersonMoveRight()

class AbstractPersonMove(ABC):

    @staticmethod
    @abstractmethod
    def move():
        """ Move """

class PersonMoveLeft(AbstractPersonMove):

    @staticmethod
    def move():
        return 'Move left'

class PersonMoveRight(AbstractPersonMove):

    @staticmethod
    def move():
        return 'Move right'


p1 = Person1()
p2 = Person2()
p1.action()
p2.action()
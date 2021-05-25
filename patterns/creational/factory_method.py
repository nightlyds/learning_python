from abc import ABC, abstractmethod

class AbstractPerson(ABC):

    @abstractmethod
    # Factory method
    def choose_side(self):
        pass

    @abstractmethod
    def action(self):
        pass


class Person1(AbstractPerson):

    def __init__(self):
        self.movement = self.choose_side()

    def choose_side(self):
        return PersonMoveLeft()

    def action(self):
        print(self.movement.move())

class Person2(AbstractPerson):

    def __init__(self):
        self.movement = self.choose_side()

    def choose_side(self):
        return PersonMoveRight()

    def action(self):
        print(self.movement.move())

class AbstractPersonMove(ABC):

    @staticmethod
    @abstractmethod
    def move():
        pass

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
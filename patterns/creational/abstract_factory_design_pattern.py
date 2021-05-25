from abc import ABC, abstractmethod

class AbstractWorkPlace(ABC):

    @abstractmethod
    def speak_with_colleagues(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Office(AbstractWorkPlace):

    def speak_with_colleagues(self):
        return 'It {} to speak with the colleagues in {}'.format(Easy().level(), self.__class__.__name__)

    def eat(self):
        return 'It {} to eat in {}'.format(Hard().level(), self.__class__.__name__)

class Home(AbstractWorkPlace):

    def speak_with_colleagues(self):
        return 'It {} to speak with the colleagues at {}'.format(Hard().level(), self.__class__.__name__)

    def eat(self):
        return 'It {} to eat at {}'.format(Easy().level(), self.__class__.__name__)

class AbstractLevel(ABC):

    @staticmethod
    @abstractmethod
    def level():
        pass

class Easy(AbstractLevel):

    @staticmethod
    def level():
        return 'easy'

class Hard(AbstractLevel):

    @staticmethod
    def level():
        return 'hard'

office = Office()
home = Home()

print(office.speak_with_colleagues(), office.eat())
print(home.speak_with_colleagues(), home.eat())
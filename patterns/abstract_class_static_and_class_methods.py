from abc import ABC, abstractmethod

class AbstractPerson(ABC):

    persons = 0

    @abstractmethod
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @staticmethod
    @abstractmethod
    def age_value(age):
        """ It returns True if age more than 18 or False if it doesn`t """

    @abstractmethod
    def return_name(self):
        return self.name

    @classmethod
    @abstractmethod
    def add_persons(cls):
        """ It adds person """


class Person(AbstractPerson):

    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def age_value(age):
        return age > 18

    def return_name(self):
        return super().return_name()

    @classmethod
    def add_persons(cls):
        cls.persons += 1
        return cls.persons

p1 = Person('name', 'lastname', 19)
print(p1.age_value(19)) # It could be called by class
print(p1.return_name())
print(Person.add_persons()) # Out: 1
print(Person.add_persons()) # Out: 2
print(Person.add_persons()) # Out: 3
print(Person.add_persons()) # Out: 4

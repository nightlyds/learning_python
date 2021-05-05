from abc import ABC, abstractmethod

class IPerson(ABC):

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass

    @classmethod
    @abstractmethod
    def print_data(cls):
        pass

class PersonSingleton(IPerson):

    __instance = None

    @classmethod
    def get_instance(cls):

        if cls.__instance == None:
            PersonSingleton("Default", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @classmethod
    def print_data(cls):
        print(f"Name: {cls.__instance.name}, Age: {cls.__instance.age}")

p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()
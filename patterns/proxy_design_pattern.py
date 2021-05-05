from abc import ABC, abstractmethod

class AbstractCat(ABC):

    @abstractmethod
    def _return_name(self):
        pass

class Cat(AbstractCat):

    def __init__(self, name):
        self._name = name

    def _return_name(self):
        return self._name

class ProxyCat(AbstractCat):

    def __init__(self, cat):
        self._cat = cat

    def _return_name(self):
        return f"Proxy: {self._cat._return_name()}"

cat = Cat('Murzik')
proxy_cat = ProxyCat(cat)

print(proxy_cat._return_name())

# from abc import ABC, abstractmethod
#
# class IPerson(ABC):
#
#     @abstractmethod
#     def show_name(self):
#         """ Show name """
#
# class Person(IPerson):
#
#     def show_name(self):
#         return "and that`s person`s method"
#
# class ProxyPerson(IPerson):
#
#     def __init__(self):
#         self.person = Person()
#
#     def show_name(self):
#         print(f'Proxy functionality {self.person.show_name()}')
#
# p1 = Person()
# print(p1.show_name())
#
# p2 = ProxyPerson()
# p2.show_name()

# from abc import ABC, abstractmethod
#
# class AbstractZoo(ABC):
#
#     @abstractmethod
#     def add_animal(self, animal):
#         """ Add Animal """
#
# class Zoo(AbstractZoo):
#
#     def __init__(self):
#         self.animals = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#
# class ProxyZoo(AbstractZoo):
#
#     def __init__(self, zoo):
#         self.zoo = zoo
#
#     def add_animal(self, animal):
#
#         print(f"Adding new animal: {animal} to: {self.zoo.__class__.__name__}")
#         self.zoo.add_animal(animal)
#
# zoo = Zoo()
# proxy_zoo = ProxyZoo(zoo)
#
# proxy_zoo.add_animal('hawk')
# proxy_zoo.add_animal('bear')
# proxy_zoo.add_animal('lark')
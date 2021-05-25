from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):

    @abstractproperty
    def product(self) -> Any:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class Product:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}")


class ConcreteBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()

        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA")

    def produce_part_b(self) -> None:
        self._product.add("PartB")

    def produce_part_c(self) -> None:
        self._product.add("PartC")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self._builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()


director = Director()
builder = ConcreteBuilder()
director.builder = builder

print("Standart basic product: ")
director.build_minimal_viable_product()
builder.product.list_parts()

print("\n")

print("Standart full featured product: ")
director.build_full_featured_product()
builder.product.list_parts()

print("\n")

# The Builder pattern can be used without a Director class
print("Custom product: ")
builder.produce_part_a()
builder.produce_part_b()
builder.product.list_parts()
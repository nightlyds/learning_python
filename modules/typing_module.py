from typing import Dict, List, Tuple, NoReturn, Any, Sequence, Optional, Union, TypeVar, Generic

# check variables
string: str = ''
number: int = 1
boolean: bool = True

list_impl: list = []
tuple_impl: tuple = ()
dictionary: dict = {}

# check sequences and elements inside
list_strings: List[str] = ['']
tuple_numbers: Tuple[int] = (1,)
dictionary_number_string: Dict[int, str] = {1: ''}

# NoReturn
def no_return() -> NoReturn:
    pass

# Sequence
def sequence(sequence: Sequence) -> Sequence:
    return sequence

# Any
def any(any: Any) -> Any:
    return any

# Optional and Union
# Optional - if it exists
# Union - one or another
def optional(arg1: Optional[int] = None) -> Union[None, int]:
    if arg1:
        return arg1
    return None

# TypeVar
# Give possibility to check types with the variable
T = TypeVar("T", int, float)

def add(x: T, y: T) -> T:
    return x + y

print(add(1, 2))
print(add(1., 2.))

L = TypeVar("L")

# Generic
# The type depends from the input data
class Foo(Generic[L]):
    def __init__(self, foo: L) -> None:
        self.foo = foo

    def get(self) -> L:
        return self.foo

f: Foo[str] = Foo("Foo")
v: str = f.get()
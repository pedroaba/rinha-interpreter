from src.enums.kind import Kind
from src.kinds.location import Location
from src.kinds.generics.primitive import Primitive, T


class Bool(Primitive[bool]):
    def __init__(self, kind: Kind, value: T, location: Location):
        super().__init__(kind, value, location)

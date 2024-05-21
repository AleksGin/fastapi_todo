from typing import Protocol

# class Stream(Protocol):
#     def read(self, size: int) -> str:
#         pass


# class AnotherStream():
#     def read(self, size: int) -> str:
#         return f'Response {size}'


# def get_value(obj: Stream, size: int):
#     print(obj.read(size=size))

# get_value(obj=AnotherStream(), size=100)


# class Iphone(Protocol):
#     price: int = 100000
#     version: str


# class Product:
#     def __init__(self, name: str, price: int, version: str):
#         self.name = name
#         self.price = price
#         self.version = version


# def summary(items: list[Iphone]) -> float:
#     return sum(item.price for item in items)


# total = summary(
#     [
#         Product("A", 10000, "29"),
#         Product('B', 12332, '23')
#     ]
# )

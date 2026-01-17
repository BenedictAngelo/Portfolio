# object = A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects
#
#           class = (blueprints) used to design the structure and layout of an object
from classes import Car

car1 = Car("Skyline GTR", "Blue", 2025, True)

print(car1)
print(car1.model)
print(car1.color)
print(car1.year)
print(car1.for_sale)
car1.drive()
car1.stop()

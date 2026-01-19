# class variables = Shared among all instances of class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Planes:

    year_manufactured = 2026
    quantity = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type
        Planes.quantity += 1

plane1 = Planes("F22 Raptor","Fighter")
plane2 = Planes("Mig 25 Foxbat", "Interceptor")
plane3 = Planes("AC-130", "Gunship")
plane4 = Planes("A10 Warthog", "Ground Support")


print(f"In year {Planes.year_manufactured}, {Planes.quantity} planes are produced")
print(plane1.name, plane1.type)
print(plane2.name, plane2.type)
print(plane3.name, plane3.type)
print(plane4.name, plane4.type)
print(Planes.quantity)

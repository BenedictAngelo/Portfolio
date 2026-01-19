# inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)


class Plane:
    def __init__(self, name):
        self.name = name
        self.is_produced = True
    
    def in_service(self):
        print(f"{self.name} is in service")


    def is_flying(self):
        print(f"{self.name} is flying")

class F22(Plane):
    def motto(self):
        print("Stealth is king")
    pass


class F35(Plane):
    def motto(self):
        print("Do all, win all")
    pass


class F15EX(Plane):
    def motto(self):
        print("Old and reliable")
    pass

fighter = F22("F22 Raptor")
omnirole = F35("F35 Lightning 2")
bomber = F15EX("F15EX Golden eagle")

print(fighter.name)
print(omnirole.name)
print(bomber.name)
print()
print(fighter.is_produced)
fighter.in_service()
fighter.is_flying()
print()
print(omnirole.is_produced)
omnirole.in_service()
omnirole.is_flying()
print()
print(bomber.is_produced)
bomber.in_service()
bomber.is_flying()
print()
fighter.motto()
omnirole.motto()
bomber.motto()

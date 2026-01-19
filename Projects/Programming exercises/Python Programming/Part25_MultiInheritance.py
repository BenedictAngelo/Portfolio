# multiple inheritance = inherit from more than one parent class
#                           C(A,B)
#
#multilevel inheritance = inherit from a parent which inherits from another parent
                        #   C(B) <- B(A) <- A


class Plane:
    def __init__(self, name):
        self.name = name

    def landing(self):
        print(f"The {self.name} is landing")
        
    def takeoff(self):
        print(f"This {self.name} is taking off")

class Fighter(Plane):
    def description(self):
        print(f"The {self.name} is for air dominance")

class Bomber(Plane):
    def description(self):
        print(f"The{self.name} is for ground support")

class Interceptor(Plane):
    def description(self):
        print(f"The {self.name} is for escort")
    
class F22(Fighter):
    pass

class F35(Bomber):
    pass

class F15(Interceptor):
    pass

f22 = F22("F22 Raptor")
f35 = F35("F 35 Lightning II")
f15 = F15("F15EX")

f22.description()
f35.description()
f15.description()

"""
--->  base class / parent class   <----

# OOP 4 basic principles:
1. INHERITANCE
2. POLYMORPHISM
3. ABSTRACTION
4. ENCAPSULATION

"""
#  Models, Photos, Specs & Engines (1968-Present)

class Opel:

    def __init__(self, year, fuel):
        self.year = year
        self.fuel = fuel

    def speed_check(self):
        print("220 km/h")

    def break_check(self):
        print("5 m")

    def describe(self):
        print(f"The car is made in {self.year} and is use {self.fuel} power")


class CorsaOpel(Opel):

    """
    To add new properties:
     1. We expand the list of parameters that the __init__ method can take them.
     2. We call the __init__ from the parent class, using super(), with the necessary parameters for the parent class.
    """

    def __init__(self, year, fuel, sound, color):
        super().__init__(year, fuel)
        self.sound = sound
        self.color = color

    def describe(self):
        print(f"The color of that car is {self.color}")
        print(f"That car make {self.sound} sound")

# child class ---> inheritance from  class Opel


class AstraOpelH(Opel):

    def motor_check(self):
        print("1923 r/m")


car4 = Opel(year=2023, fuel="diesel")
# print(car4.fuel)
# print(car4.year)
# car4.describe()

car5 = CorsaOpel(year=2000,
                 fuel="benzine",
                 sound="nino-mimo",
                 color="red")

print(car5.year)
print(car5.fuel)
print(car5.sound)
print(car5.color)

car5.describe()


class AstraOpelG(Opel):

    def pollution_check(self):
        print("23 µg/m3")

#
# car1 = Opel(2022)
# car1.speed_check()
# car1.break_check()
# print(car1.year)
#
#
# car2 = AstraOpelH(2023)
# car2.motor_check()
# # other method from parent class
#
# car2.speed_check()
# car2.break_check()
# print(car2.year)
#
# car3 = AstraOpelG(2024)
# car3.pollution_check()
# #
# car3.speed_check()
# car3.break_check()
# print(car3.year)



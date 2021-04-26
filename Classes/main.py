class AmazingDog:

    animal_kind = "canine"

    def bark(self):
        return "woof!"


variable1 = AmazingDog()
print(variable1.animal_kind)
print(variable1.bark())


variable1.animal_kind = "Dolphin"
print(variable1.animal_kind)
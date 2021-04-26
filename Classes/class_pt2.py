class AmazingDog:

    def __init__(self, animal_kind):
        self.animal_kind = animal_kind
        __is_alive = False

    def bark(self):
        return "woof!"

    def set_is_alive(self, alive: bool):
        self.__is_alive = alive

    def get_is_alive(self):
        return self.__is_alive

Bob = AmazingDog("canine") # initialized these objects with these attributes "canine" and "dolphin"
Sue = AmazingDog("dolphin")
print(Bob.animal_kind)
print(Sue.animal_kind)
print(Bob.bark())
Bob.set_is_alive(True)
print(Bob.get_is_alive())
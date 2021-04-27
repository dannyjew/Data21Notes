from Animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        print("if i have venom, i'm going to use it")

    def moving(self):
        print("moving but as a snake")

    def __repr__(self):
        return f"This is a reptile" # this changes the representation of this class

bob = Reptile()
cat = Animal()

bob.breathe()
bob.use_venom()
bob.moving() # uses function from sub class

cat.moving() # uses function from class

print(bob)
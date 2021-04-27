class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("one breath in and one out")

    def eating(self):
        print("nom nom nom")

    def moving(self):
        print("Forwards, Backwards and side to side")


print(__name__)
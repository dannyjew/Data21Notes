class Car:

    def __init__(self, car_type: str, max_speed: str):
        self._car_type = car_type
        self.__max_speed = max_speed
        self.__current_speed = "0"

    def accelerate(self, speed_increase: str) -> str:
        if self.__current_speed + speed_increase <= self.__max_speed:
            self.__current_speed = str(int(self.__current_speed) + int(speed_increase))
            print("Your current speed is "+str(self.__current_speed))
        else:
            self.__current_speed = self.__max_speed
            print("You have reached the max speed! ")

    def get_current_speed(self):
        return self.__current_speed


car_type = input("WHat car do you want to drive? ")
max_speed = input("What is the max speed? ")
car = Car(car_type, max_speed)

acceleration = input("Accelerate to what speed? ")
current_speed = "0"
counter = 1 #first run allow 0

while int(current_speed) > 0 or counter == 1:
    accelerate = input("Accelerate by how much? ")
    car.accelerate(accelerate)
    current_speed = car.get_current_speed()
    counter = counter + 1


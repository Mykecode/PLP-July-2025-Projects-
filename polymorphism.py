class Vehicle:
    def move(self):
        print('Vehicle is moving....')
    
class Train(Vehicle):
    def move(self):
        print('The train is moving...')
        
class Airplane(Vehicle):
    def move(self):
        print('The airplane is flying...')
      
class Boat(Vehicle):
    def move(self):
        print('The boat is sailing smoothly...')
        
class Car(Vehicle):
    def move(self):
        print('The car is driving smoothly...')

train = Train()
plane = Airplane()
boat = Boat()
car = Car()

train.move()
plane.move()
boat.move()
car.move()

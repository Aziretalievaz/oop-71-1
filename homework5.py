
class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")


class Electriccar(Vehicle):
    def start(self):
        super().start()


class Tesla(Electriccar, Car):
    def start(self):
        super().start()
        print("Tesla ready")


tesla = Tesla()
tesla.start()



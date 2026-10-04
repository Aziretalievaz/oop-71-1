class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


    def drive(self):
        print("Mashina edet")


car1 = Car("Toyota", 2003)
car2 = Car("BMW", 2015)

print(car1.brand, car1.year)
print(car2.brand, car2.year)

car1.drive()


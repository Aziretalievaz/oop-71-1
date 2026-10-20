
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст должен быть положительным")
        self.__age = age

    def make_sound(self):
        print("Животное издает звук")


class Dog(Animal):
    def make_sound(self):
        print("гафгаф")


class Cat(Animal):
    def make_sound(self):
        print("мяйу")



dog = Dog("REX", 3)
cat = Cat("Пусик", 2)

dog.make_sound()
cat.make_sound()

print(dog.get_name())
print(dog.get_age())

print(cat.get_name())
print(cat.get_age())

cat.set_age(2)
cat.set_name("Киса")

print(cat.get_name())
print(cat.get_age())

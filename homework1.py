class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce (self):
        print("Menya zovut", self.name, "Data moego rojdeniya", self.birth_date, "Po professii ya", self.occupation, "Obrazovanie", self.higher_education)

person1 = Person("Azim", "15.05.1994", "manager", True)
person2 = Person("Bakyt", "15.05.1992", "ingener", False)

person1.introduce()
person2.introduce()
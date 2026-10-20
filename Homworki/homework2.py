class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Menya zovut {self.name}, Data moego rojdeniya {self.birth_date}, Po professii ya {self.occupation}, Obrazovanie {self.higher_education}")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Меня зовут {self.name}, Дата моего рождения {self.birth_date}"
            f"По профессии я {self.occupation}, Образование {self.higher_education}",
            f"Я одноклассник, моя группа {self.group_name}"
            )



class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(
            "Меня зовут", self.name,
            "Дата моего рождения", self.birth_date,
            "По профессии я", self.occupation,
            "Образование", self.higher_education,
            "Я друг, моё хобби", self.hobby
        )


classmate1 = Classmate(
    "Bektur",
    "05.12.2000",
    "programmer",
    True,
    "ПИ-21"
)

classmate2 = Classmate(
    "Aibek",
    "10.03.2001",
    "engineer",
    True,
    "ПИ-22"
)

friend1 = Friend(
    "Azamat",
    "15.05.1999",
    "manager",
    True,
    "football"
)

friend2 = Friend(
    "Nursultan",
    "20.08.1998",
    "designer",
    False,
    "gaming"
)


classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

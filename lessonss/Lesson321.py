

# # class Car:
# #     def change(self):
# #         print("Машина изменилась")

# # car = Car()
# # car.change()        



# class Bzs:
#     def __init__(self, marketing, tovar, prodaji):
#         self.marketing = marketing
#         self.tovar = tovar
#         self.prodaji = prodaji

#     def rabota(self):
#         print("Запускает таргет у нас", self.marketing, "Закупаем Товар", self.tovar, "Передаем в Отдел продаж", self.prodaji)



#     # def tovar_t(self):
#     #     print("Закупаем товар")



#     # def prodaji_t(self):
#     #     print("Передаем в отдел продаж")



# bzs1 = Bzs("Azim", "Nout booki", "Команда Бермет")  

# bzs1.rabota()




# name = "Azim"
# age = 30
# city = "Bishkek"

# print(f"My name is {name}, mne {age} let, ya jivy v gorode {city}")


# class Car:
#     def 


# def mogu(name_biz)
#     .mogu()



# def square(number):
#     return number ** 2


# print(square(5))

# def multiply(a, b):
#     return a * b



# print(multiply(5, 4))

# def greet(name, age):
#     return(f"Tebya zovut {name}, tebe {age} let")



# print(greet("Azim", 30))    


# def check_age(age):
#     if age < 18:
#         return("несовершеннолетний")
#     else: 
#         return("совершеннолетний")    


# print(check_age(5))
# print(check_age(7))


# class Bancaccount:
#     def __init__(self, login, password, balance):
#         self.login = login
#         self.password = password
#         self.balance = balance

#     def get_balance(self, user_log, user_pass):
#         if user_log == self.login and user_pass == self.password:
#             return self.balance
#         return ("Неверный логин или пароль")


#     def add_money()


# account = Bancaccount("azim", "1255", "1000")
# print(account.get_balance("azim", "1255"))
    

# name = "ainura"
# age = 53
# vopr_1 = "Ainura tebe skolko let?"

# print(name)
# print(age)
# print(vopr_1)


# name_1 = [1, 2, 3, 4]

# name_1.append(7)
# name_1.copy

# print(name_1)

# for i in range(1, 4):
#     print(i)



# prices = [30, 40, 45, 50]


# products = ["Арматура", "Труба", "Швеллер"]
# prices = [45, 120, 350]
# products.append("Уголок")

# print(products)
# print(len(products))
# # print(prices[2])
# # print(products[0])


# products = ["Арматура", "Труба", "Швеллер"]
# prices = [45, 120, 350]
# for i in range(len(products)):
#     print(products[i], "-", prices[i], "som")


# name = "Armatyra"
# price = 45
# quantity = 500

# product = {
#     "name": "Арматура",
#     "price": 45,
#     "quantity": 500
# }

# total = product["price"] * product["quantity"]

# print(f"Товар: {name}")
# print(f"Остаток: {quantity}")
# print(f"Стоимость остатка: {total}")
# def pin_guard(func): — декоратор принимает функцию.
# def wrapper(pin, money): — создаём обёртку.
# if — проверяем PIN.
# func(...) — вызываем исходную функцию, если проверка пройдена.
# return wrapper — возвращаем обёртку.
# withdraw = pin_guard(withdraw) — подключаем защиту.

# def withdraw(pin, money):
#     print("Деньги выданы!")
#     return f"Вы сняли {money} сом"

# SECRET_PIN = "4567"

# def pin_guard(func):
#     def wrapper(pin, money):
#         if pin != SECRET_PIN:
#             print("Oshibka parol ne pravilnyi")
#             return None
#         return func(pin, money)
#     return wrapper


# withdraw = pin_guard(withdraw)
# print(withdraw("1234", 500))
# print(withdraw("4567", 500))



def add(a, b):
    print(a + b)



# result = add(2, 3)
# print(result)



TRIP_COST = 20


class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0


    def get_owner(self):
        return self.__owner


    def get_balance(self):
        return self.__balance


    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount


    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            raise ValueError("Недостаточно средств на карте")
        self.__balance -= TRIP_COST



card1 = TransportCard("Азим")
card2 = TransportCard("Айбек")

card1.add_money(100)
print(card1.get_owner())
print(card1.get_balance())
card1.pay_for_trip()
print(card1.get_balance())

try:
    card2.pay_for_trip()
except ValueError as error:
    print(error)

try:
    card1.add_money(-50)
except ValueError as error:
    print(error)
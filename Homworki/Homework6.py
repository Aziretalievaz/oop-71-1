
def open_vault(password, money):
    print("Сейф открыт!")
    return f"Забирайте {money} сом"


SECRET_PASSWORD = "kitty_2007"

def password_guard(func):
    def wrapper(password, money):
        if password != SECRET_PASSWORD:
            print("🚨 СИГНАЛИЗАЦИЯ! Доступ запрещён")
            return None

        return func(password, money)

    return wrapper


open_vault = password_guard(open_vault)

print(open_vault("123", 100))
print(open_vault("kitty_2007", 1000000000000))

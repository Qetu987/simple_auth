from app.login import auth
from app.register import register

def main():
    print("********************")
    print("Вітаю! Виберіть потрібний пункт")
    print("1. Авторизація")
    print("2. Реєстрація")
    print("********************")

    ch = str(input("Введіть свій вибір (1 або 2): "))

    if ch == "1":
        ans = auth()
    else:
        ans = register()
        
    print(ans)

if __name__ == '__main__':
    main() 

from app.validators import check_username_len

def auth() -> dict:
    username = input("Введіть ім`я користувача: ").lower()
    password = input("Введіть пароль: ")

    if check_username_len(username):
        with open('db/logins.txt', 'r', encoding='utf-8') as f:
            username_list = f.read().split('\n')
            username_list.pop()

        with open('db/passwords.txt', 'r', encoding='utf-8') as f:
            password_list = f.read().split('\n')
            password_list.pop()

        if (username in username_list) and (password in password_list):
            if username_list.index(username) == password_list.index(password):
                return {'type':'Done', 'text':'User has been logined'}
            else:
                return {'type':'Error', 'text':'Creds is not valid.'}
        else:
            return {'type':'Error', 'text':'Creds is not valid.'}
    else:
        return {'type':'Error', 'text':'Username is not valid.'}
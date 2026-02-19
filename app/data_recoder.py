def create_profile(username:str, password:str) -> None:
    with open('db/logins.txt', 'a', encoding='utf-8') as f:
        f.write(username + '\n')

    with open('db/passwords.txt', 'a', encoding='utf-8') as f:
        f.write(password + '\n')
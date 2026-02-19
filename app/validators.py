'''
    Docstring для app.validators
    Валідація для даних введених користувачем.
'''

def check_username_len(username:str) -> bool:
    '''
    Перевірка довжини логіну.
    - True: якщо логін більше 3х символів
    - False: інакше
    '''
    return len(username) > 3

def check_length(password:str) -> bool:
    return len(password) >= 8

def check_number1(password:str) -> bool:
    return not password[0].isnumeric()

def check_spec1(password:str) -> bool:
    spec = "!@#$%^&*()-_=+"
    return password[0] not in spec

def check_spec2(password:str) -> bool:
    spec = "!@#$%^&*()-_=+"
    return any(char in spec for char in password)

def check_has_number2(password:str) -> bool:
    return any(char.isdigit() for char in password) 

def check_big_letter(password:str) -> bool:
    return any(let.isupper() for let in password) 

def check_space(password:str) -> bool:
    return " " not in password   
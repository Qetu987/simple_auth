from app.validators import (
    check_length, 
    check_number1,
    check_has_number2, 
    check_spec2,
    check_spec1, 
    check_big_letter, 
    check_space,
)

def check_password(password:str) -> bool:
    return (
        check_length(password) and check_number1(password) 
        and check_spec1(password) and check_spec2(password) 
        and check_has_number2(password) and check_big_letter(password) 
        and check_space(password)
    )

def check_username_exist(username:str) -> bool:
    with open('db/logins.txt', 'r', encoding='utf-8') as f:
        username_list = f.read().split('\n')
        username_list.pop()
        
    if username not in username_list:
        return True
    return False

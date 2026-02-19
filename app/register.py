from app.validators import check_username_len
from app.tools import (
    check_password, 
    check_username_exist
)
from app.data_recoder import create_profile


def register():
    username = input("Введіть ім`я користувача: ").lower()
    password = input("Введіть пароль: ")
    if check_password(password):
        if check_username_len(username):
            if check_username_exist(username):
                create_profile(username, password)
                return {'type':'Done', 'text':'User has been registered'}
            else:
                return {'type':'Error', 'text':'Username already exist.'}
        else:
            return {'type':'Error', 'text':'Username is not valid.'}
    else:
        return {'type':'Error', 'text':'Password is not valid.'}
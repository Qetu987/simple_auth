import xlwt
from datetime import datetime

def create_profile(username:str, password:str) -> None:
    with open('db/logins.txt', 'a', encoding='utf-8') as f:
        f.write(username + '\n')

    with open('db/passwords.txt', 'a', encoding='utf-8') as f:
        f.write(password + '\n')


def create_profile_with_xls(username:str, password:str) -> None:
    wb = xlwt.Workbook()
    ws = wb.add_sheet('User')

    wb.save(f'{username}.xls')
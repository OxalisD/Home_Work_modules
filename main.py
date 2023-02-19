from application import salary, people
from datetime import datetime
from colorama import Style, Fore, Back

if __name__ == "__main__":
    head = Fore.BLUE + Back.BLACK + Style.BRIGHT
    cont = Fore.BLACK + Back.WHITE + Style.NORMAL
    print(f'{head}Текущая дата: {datetime.today().date()}')
    print(cont + 'Функции вызваны:')
    people.get_employees()
    salary.calculate_salary()


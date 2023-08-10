import random

def Sozdanie_Login():
    log = input('Введите примерно какой вы хотите логин: ')
    letters_list = ['Just The King', 'Lunar cat', '*S~@~M~u~R~@~I*', 'Another', '™_Game®_™', 'Clear fun',
                    '{.:L.S.D:.Prizrak}~>Remix', 'Welcome to the Hell', 'Conqueror', '|~HeaDShoT~|—>',
                    'Veni.vidi.vici', 'SAN†BARRIO', 'Usman', '*Mr.Panda*', '=miller=', 'Hands grow not from Ass']
    random_index = random.randint(0, len(letters_list) - 1)
    vivod = f'{log}_{letters_list[random_index]}'
    print(f'\nВот ваш логин --> {vivod}')

def Sozdanie_Porol():
    pas = []
    v = int(input('Количество символов: '))
    while len(pas) < v:
        pasw = random.choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')
        pas.append(pasw)
    print("Ваш пароль: ", ''.join(pas))

while True:
    try:
        action = int(input('1 - Создать логин.\n2 - Создать пороль.''\n3 - Выход.''\n:)----> '))
        if action == 1:
            Sozdanie_Login()
        elif action == 2:
            Sozdanie_Porol()
        elif action == 3:
            exit()
    except NameError:
        print('\nВы ввели неверное значение')
        input('Enter для продолжения: ')

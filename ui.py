from logger import input_data, print_data, put_data, delete_data


def interface():
    print('Добрый день! Это бот-помощник. \n'
    'Что вы хотите сделать?\n'
    '1 - Записать данные\n'
    '2 - Вывести данные\n'
    '3 - Изменить данные\n'
    '4 - Удалить данные\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 4:
        print('Ещё один шанс! Ваш выбор:')
        command = int(input("Введите номер операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()

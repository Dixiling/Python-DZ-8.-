def name_input():
    return input('Введите имя: ').title()


def surname_input():
    return input('Введите фамилию: ').title()


def patronymic_input():
    return input('Введите отчество: ').title()


def phone_input():
    return input('Введите номер: ')


def address_input():
    return input('Введите адрес: ').title()


def create_contact():
    '''Add an entry'''
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone} {address}\n'

def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a' , encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан!\n')

def print_contacts():
    '''List all entries'''
    with open('phonebook.txt', 'r' , encoding='utf-8') as file:
        print('----------------------')
        print(file.read())
        print('----------------------')
    # with open('phonebook.txt', 'r' , encoding='utf-8') as file:
    #     contacts_list = file.read().rstrip().split('\n\n')
    #     for nn , contact in enumerate(contacts_list, 1):
    #         print(f'{nn}. {contact}\n')

def search_contact(field=''):
    ''''''
    print(
        'Возможные варианты поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру\n'
        '5. по городу\n'
        )

    index_var = int(input('Введите вариант поиска: '))-1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = contacts_str.rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')

def copy_line():
    
    with open('phonebook.txt', 'r' , encoding='utf-8') as file:
        lines = file.readlines()

    line_number = int(input('Введите номер данных для копии: ')) 

    with open('phonebook1.txt', 'a' , encoding='utf-8') as file:
        file.write(lines[line_number - 1])

    print('\nУспешное копирование\n')

def interface():
    with open('phonebook.txt', 'a'):
        pass


    user_input = None
    while user_input != '5':
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Копирование данных\n'
            '5. Выход из программы\n'
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4' , '5'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_line()
        
if __name__ == '__main__':
    interface()
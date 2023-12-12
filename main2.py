def copy_line(sourse_file, tagret_file , line_number):
    with open(sourse_file, 'r' , encoding='utf-8') as file:
        lines = file.readlines()

    if line_number < 1 or line_number > len(lines):
        print('Некорректный ввод')
        return
    
    with open(tagret_file, 'w' , encoding='utf-8') as file:
        file.write(lines[line_number - 1])


        for i in range(len(lines)):
            if i != line_number - 1:
                file.write(lines[i])

    print('Успешное копирвоание')

sourse_file = 'phonebook.txt'

tagret_file = 'phonebook1.txt'

line_number = int(input('Введите строку:'))

copy_line(sourse_file , tagret_file , line_number)

# 2ой вариант
# import csv

# with open('phonebook.txt' , 'r' , encoding='utf-8') as file:
#     reader = csv.reader(file)
#     data = list(reader)

# row_number = int(input("Введите номер строки: ")) - 1

# with open('phonebook1.txt', 'w', newline='') as file:
#     writer =csv.writer(file)
#     writer.writerow(data[row_number])

# print("Строка сохранена в файл phonebook1.txt")
import csv
import os
from datetime import datetime


def createFile(filename):
    if not filename.endswith('.csv'):
        filename = filename + '.csv'

    if not os.path.exists(filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'note'])
            writer.writeheader()
            print(f'Файл {filename} создан.')
    else:
        print(f'Файл {filename} уже существует.')


def readFile(filename):
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row['date'], row['note'])
    else:
        print(f'Файл {filename} не найден.')


def writeFile(filename, note):
    if os.path.exists(filename):
        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'note'])
            writer.writerow({'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'note': note})
            print('Заметка добавлена.')
    else:
        print(f'Файл {filename} не найден.')


def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'Файл {filename} удален.')
    else:
        print(f'Файл {filename} не найден.')


def editNote(filename, date_to_edit, new_note):
    rows = []
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['date'] == date_to_edit:
                    row['note'] = new_note
                rows.append(row)

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'note'])
            writer.writeheader()
            writer.writerows(rows)

        print('Заметка отредактирована.')
    else:
        print(f'Файл {filename} не найден.')


def selectByDate(filename, date_to_select):
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['date'] == date_to_select:
                    print(row['date'], row['note'])
                    return
        print('Запись не найдена.')
    else:
        print(f'Файл {filename} не найден.')


while True:
    action = input('Выберите действие (create, read, write, delete, edit, select, exit): ')

    actions = {
        'create': lambda: createFile(input('Введите имя файла: ')),

        'read': lambda: readFile(input('Введите имя файла с расширением .csv: ')),

        'write': lambda: writeFile(input('Введите имя файла с расширением .csv: '),
                                   input('Введите заметку: ')),

        'delete': lambda: deleteFile(input('Введите имя файла с расширением .csv: ')),

        'edit': lambda: editNote(input('Введите имя файла с расширением .csv: '),
                                 input('Введите дату записи для редактирования (гггг-мм-дд чч:мм:сс): '),
                                 input('Введите новую заметку: ')),

        'select': lambda: selectByDate(input('Введите имя файла с расширением .csv: '),
                                       input('Введите дату записи для выборки (гггг-мм-дд чч:мм:сс): ')),

        'exit': lambda: exit(),
    }

    selected_action = actions.get(action)
    if selected_action:
        selected_action()
    else:
        print('Некорректное действие. Попробуйте снова.')


import os

programmers = []

with open('programmers.txt', 'r') as file:
    someProgrammers = file.readlines()
    programmers = [x.strip('\n') for x in someProgrammers]

while True:
    print('Добро пожаловать в программу управления проектами')
    print('1. Добавить программиста')
    print('2. Удалить программиста')
    print('3. Показать список программистов')
    print('4. Проверка наличия программиста на проекте')
    print('5. Завершить работу')

    choice = input('Выберите действие: ')
    if choice == '1':
        programmer = input('Введите имя программиста: ')
        programmers.append(programmer)
        programmers.sort()
        print(f"Программист {programmer} добавлен в список программистов")
        with open('programmers.txt', 'w') as file:
            file.writelines([programmer + '\n' for programmer in programmers])
    elif choice == '2':
        programmer = input('Введите имя программиста: ')
        if programmer in programmers:
            programmers.remove(programmer)
            print(f"Программист {programmer} удален из списка программистов")
        else:
            print("Программиста нет в списке")
    elif choice == '3':
        print(programmers)
    elif choice == '4':
        programmer = input('Введите имя программиста: ')
        if programmer in programmers:
            print("Программист на проекте")
        else:
            print("Программиста нет в списке")
    elif choice == '5':
        break
    else:
        print('Неверный выбор')

    os.system('pause')
    os.system('cls')

print('Программа завершена')

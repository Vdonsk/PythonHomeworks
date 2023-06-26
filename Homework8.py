def input_dataset():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    return surname, name, phone

def controller():
    mode = int(input('Выберите режим:\n1 - поиск контакта\n2 - добавить контакт\nВведите режим: '))
    if mode == 1:
        surname = inp_surname()
        find_person(surname)
    if mode == 2:
        dataset = input_dataset()
        write_person(dataset)

def find_person(surname: str):
    with open('PythonHomeworks\phone.txt', 'r', encoding='utf-8') as file:
        line_list = file.read().splitlines()
        for ind in range(len(line_list)):
            if line_list[ind] == surname.title():
                print(line_list[ind])
                print(line_list[ind + 1])
                print(line_list[ind + 2])                       

def inp_surname():
    surname = input('Поиск по фамилии: ')
    return surname

def write_person(dataset: tuple):
       with open('PythonHomeworks\phone.txt', 'a', encoding='utf-8') as file:
        file.write('\n\n' + '\n'.join(dataset))

controller()
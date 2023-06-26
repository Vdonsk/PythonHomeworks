def input_dataset():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    return surname, name, phone

def controller():
    mode = int(input('Выберите режим: 1 - поиск контакта, 2 - добавить контакт: '))
    if mode == 1:
        surname = inp_surname()
        find_person(surname)
    elif mode == 2:
        dataset = input_dataset()
        write_person(dataset)
    else:
        print('Такого режима не существует')
        controller()

def find_person(surname: str):
    with open('PythonHomeworks\phone.txt', 'r', encoding='utf-8') as file:
        line_list = file.read().splitlines()
        for ind in range(len(line_list)):
            if line_list[ind] == surname.title():
                print(line_list[ind])
                print(line_list[ind + 1])
                print(line_list[ind + 2])             
                
def inp_surname():
    surname = input('Введите фамилию для поиска контакта: ')
    return surname

def write_person(dataset: tuple):
       with open('PythonHomeworks\phone.txt', 'a', encoding='utf-8') as file:
        file.write('\n\n' + '\n'.join(dataset))

controller()
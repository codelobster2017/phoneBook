from copy import deepcopy

PATH = 'phones.txt'
phone_book = {}
original_book = {}


def create_file():
    global PATH
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('')

def open_file():
    global phone_book, original_book, PATH
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        phone_book[i] = contact
    original_book = deepcopy(phone_book)

def save_file():
    global phone_book
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_contact(new_contact: list[str]):
    global phone_book
    if not phone_book:
        c_id = 1
    else:
        c_id = max(phone_book) + 1
    phone_book[c_id] = new_contact

def find_contact(word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for c_id, contact in phone_book.items():
        for field in contact:
            if word.lower() in field.lower():
                result[c_id] = contact
                break
    return result

def edit_contact(c_id: int, new_contact: list[str]):
    global phone_book
    current_contact = phone_book.get(c_id)
    contact = []
    for i in range(len(new_contact)):
        if new_contact[i]:
            contact.append(new_contact[i])
        else:
            contact.append(current_contact[i])
    phone_book[c_id] = contact
    return contact[0]

def delete_contact(c_id: int) -> str:
    global phone_book
    return phone_book.pop(c_id)[0]
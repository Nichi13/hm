import json
import os


class Contact:
    # сделал ввод данных, хотел через args получать доп номера
    # но почему-то он не хочет открывать их
    def __init__(self, name, second_name, phone_number, elected=False, *number, **data):
        self.name = name
        self.second_name = second_name
        self.phone_number = phone_number
        self.elected = elected
        self.data = data
        self.number = number

    def str(self):
        cont = ('Имя : {}\nФамилия : {}\nТелефон : {}\n'
        .format(self.name, self.second_name, self.phone_number,))
        if self.elected is True:
            cont += 'В избранных : да\n'
        else:
            cont += 'В избранных : нет\n'
        cont += 'Дополнительная информация : \n'
        if 'email' in self.data:
            cont += '       email : {}\n'.format(self.data['email'])
        if 'telegram' in self.data:
            cont += '       telegram : {}'.format(self.data['telegram'])

        return cont

    def contact_data(self):
        contact_dict = {}
        contact_dict['name'] = self.name
        contact_dict['second_name'] = self.second_name
        contact_dict['phone_number'] = self.phone_number
        contact_dict['telegram'] = self.data['telegram']
        if 'email' in self.data:
            contact_dict['email'] = self.data['email']
        if 'telegram' in self.data:
            contact_dict['elected'] = self.elected
        return contact_dict


class PhoneBook:

    def __init__(self, book_name):
        self.book_name = book_name

    def add_contact(self, contact):
        contact_dict = contact.contact_data()
        phone_book = []
        phone_book.append(contact_dict)
        size = os.stat('phone_book.json').st_size == 0
        if size:
            with open('phone_book.json', 'w', encoding='utf-8') as file:
                json.dump(phone_book, file, indent=4, ensure_ascii=False)
        else:
            with open('phone_book.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                if contact_dict in data:
                    print('Уже имеется такой контакт')
                else:
                    data.append(contact_dict)
                    with open('phone_book.json', 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
        pass

    def print_contact(self, contact):
        print(contact.str())

    def del_contact(self, number):
        with open('phone_book.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                if number == i['phone_number']:
                    data.remove(i)
                    with open('phone_book.json', 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
    pass

    def search_by_favorites(self):
        with open('phone_book.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                if i['elected']:
                    print('{} {}: {} - находится в избранных'.format(i['name'], i['second_name'], i['phone_number']))

    def search_by_name(self, name, second_name):
        with open('phone_book.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                if i['name'] == name and i['second_name'] == second_name:
                    print('{} {}: {} '.format(i['name'], i['second_name'], i['phone_number']))


if __name__ == '__main__':
    vas = Contact('Вася', 'Обломов', '+7529798456', elected=True, telegram='@Obl', email='obl@gmil.com')
    fil = Contact('Филипп', 'Годунов', '+7984561', elected=False, telegram='@God')
    gor = Contact('Жора', 'Годунов', '1', elected=True, telegram='@God')
    p = PhoneBook('f')
    p.add_contact(vas)
    p.add_contact(fil)
    p.add_contact(gor)
    p.search_by_name('Вася', 'Обломов')
    p.search_by_favorites()
    p.del_contact('1')
    p.print_contact(vas)


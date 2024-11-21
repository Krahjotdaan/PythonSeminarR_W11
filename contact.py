import json
import uuid
import csv

NOTES_FILE = "contacts.json"

class Contact:
    def __init__(self):
        self.contacts = {}

    def create_contact(self):
        name = input("Введите имя: ")
        number = input("Введите номер: ")
        email = input("Введите email: ")
        id = str(uuid.uuid4())
        new_contact = {
            "id": id,
            "name": name,
            "number": number,
            "email": email
        }
        self.contacts[id] = new_contact

    def edit_contact(self, id):
        try:
            new_name = input("Введите имя: ")
            new_number = input("Введите номер: ")
            new_email = input("Введите email: ")
            self.contacts[id]['name'] = new_name
            self.contacts[id]['number'] = new_number
            self.contacts[id]['email'] = new_email
        except Exception as e:
            print(f"Ошибка: {e}")

    def delete_contact(self, id):
        try:
            del self.contacts[id]
        except Exception as e:
            print(f"Ошибка: {e}")

    def load_contacts(self):
        try:
            with open(NOTES_FILE, "r") as f:
                self.contacts = json.load(f)
        except Exception as e:
            print(f"Ошибка: {e}")
            return []
        
    def view_contact_by_name(self):
        name = input("Введите имя: ")
        for contact in self.contacts.values():
            if contact['name'] == name:
                print(contact)

    def view_contact_by_number(self):
        number = input("Введите номер: ")
        for contact in self.contacts.values():
            if contact['number'] == number:
                print(contact)

    def save_contacts(self):
        with open(NOTES_FILE, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def export_contacts_csv(self, filename="contacts.csv"):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'name', 'number', 'email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows([contact for contact in self.contact.values()])
            print(f"Заметки экспортированы в файл {filename}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def import_contacts_csv(self, filename="contacts.csv"):
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                new_contacts = [row for row in reader]
            self.contacts = new_contacts
        except Exception as e:
            print(f"Ошибка: {e}")
            return []

    def manage_contacts(self):
        from personal_assistant import main

        self.load_contacts()
        while True:
            print("\nМеню управления контактами:")
            print("1. Создать контакт")
            print("2. Найти контакт по имени")
            print("3. Найти контакт по номеру")
            print("4. Изменить контакт")
            print("5. Удалить контакт")
            print("6. Экспорт в CSV")
            print("7. Импорт из CSV")
            print("8. Назад")

            choice = input("> ")
            if choice == '1':
                self.create_contact()
            elif choice == '2':
                self.view_contact_by_name()
            elif choice == '3':
                self.view_contact_by_number()
            elif choice == '4':
                id = input('Введите id: ')
                self.edit_contact(id)
            elif choice == '5':
                id = input('Введите id: ')
                self.delete_contact()
            elif choice == '6':
                self.export_contacts_csv()
                self.save_contacts()
            elif choice == '7':
                self.import_contacts_csv()
                self.save_contacts()
            elif choice == '8':
                main()
            else:
                print("Неверный выбор.")
                self.manage_contacts()
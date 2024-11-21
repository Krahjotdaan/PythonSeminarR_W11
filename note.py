import json
import uuid
import csv
from datetime import datetime

NOTES_FILE = "notes.json"

class Note:
    def __init__(self):
        self.notes = {}

    def create_note(self):
        title = input("Введите заголовок: ")
        content = input("Введите текст заметки: ")
        id = str(uuid.uuid4())
        new_note = {
            "id": id,
            "title": title,
            "content": content,
            "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        self.notes[id] = new_note

    def edit_note(self, id):
        try:
            new_title = input('Новый заголовок: ')
            new_content = input('Новый текст: ')
            self.notes[id]['title'] = new_title
            self.notes[id]['content'] = new_content
        except Exception as e:
            print(f"Ошибка: {e}")

    def delete_note(self, id):
        try:
            del self.notes[id]
        except Exception as e:
            print(f"Ошибка: {e}")

    def load_notes(self):
        try:
            with open(NOTES_FILE, "r") as f:
                self.notes = json.load(f)
        except Exception as e:
            print(f"Ошибка: {e}, 29")
            return []
        
    def view_notes(self):
        for note in self.notes:
            print(note)

    def save_notes(self):
        with open(NOTES_FILE, "w") as f:
            json.dump(self.notes, f, indent=2)

    def export_notes_csv(self, filename="notes.csv"):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'title', 'content', 'timestamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows([note for note in self.notes.values()])
            print(f"Заметки экспортированы в файл {filename}")
        except Exception as e:
            print(f"Ошибка: {e}, 49")

    def import_notes_csv(self, filename="notes.csv"):
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                new_notes = [row for row in reader]
            self.notes = new_notes
        except Exception as e:
            print(f"Ошибка: {e}, 58")
            return []

    def manage_notes(self):
        from personal_assistant import main

        self.load_notes()
        while True:
            print("\nМеню управления заметками:")
            print("1. Создать заметку")
            print("2. Просмотреть список заметок")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Экспорт в CSV")
            print("6. Импорт из CSV")
            print("7. Назад")

            choice = input("> ")
            if choice == '1':
                self.create_note()
            elif choice == '2':
                self.view_notes()
            elif choice == '3':
                id = input('Введите id: ')
                self.edit_note(id)
            elif choice == '4':
                id = input('Введите id: ')
                self.delete_note(id)
            elif choice == '5':
                self.export_notes_csv()
            elif choice == '6':
                self.import_notes_csv()
                self.save_notes()
            elif choice == '7':
                main()
            else:
                print("Неверный выбор.")
                self.manage_notes()
                
import json
import uuid
import csv

NOTES_FILE = "tasks.json"

class Task:
    def __init__(self):
        self.tasks = {}

    def create_task(self):
        title = input("Введите заголовок: ")
        content = input("Введите описание: ")
        id = str(uuid.uuid4())
        done = False
        priority = input("Введите приоритет (высокий, средний, низкий): ")
        due_date = input("Введите срок выполнения в формате ДД-ММ-ГГГГ: ")
        new_task = {
            "id": id,
            "title": title,
            "content": content,
            "done": done,
            "priority": priority,
            "due_date": due_date
        }
        self.tasks[id] = new_task

    def edit_task(self, id):
        try:
            new_title = input("Введите заголовок: ")
            new_content = input("Введите описание: ")
            new_priority = input("Введите приоритет (высокий, средний, низкий): ")
            new_due_date = input("Введите срок выполнения в формате ДД-ММ-ГГГГ: ")

            self.tasks[id]['title'] = new_title
            self.tasks[id]['content'] = new_content
            self.tasks[id]['priority'] = new_priority
            self.tasks[id]['due_date'] = new_due_date
        except Exception as e:
            print(f"Ошибка: {e}")

    def delete_task(self, id):
        try:
            del self.tasks[id]
        except Exception as e:
            print(f"Ошибка: {e}")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def done_task(self, id):
        self.tasks[id]['done'] = True
        print('Задача выполнена')

    def load_tasks(self):
        try:
            with open(NOTES_FILE, "r") as f:
                self.tasks = json.load(f)
        except Exception as e:
            print(f"Ошибка: {e}")
            return []

    def save_tasks(self):
        with open(NOTES_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def export_tasks_csv(self, filename="tasks.csv"):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'title', 'content', 'timestamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows([task for task in self.tasks.values()])
            print(f"Заметки экспортированы в файл {filename}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def import_tasks_csv(self, filename="tasks.csv"):
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                new_tasks = [row for row in reader]
            self.tasks = new_tasks
        except Exception as e:
            print(f"Ошибка: {e}")
            return []

    def manage_tasks(self):
        from personal_assistant import main

        self.load_tasks()
        while True:
            print("\nМеню управления задачами:")
            print("1. Создать задачу")
            print("2. Просмотреть список задач")
            print("3. Редактировать задачу")
            print("4. Удалить задачу")
            print("5. Выполнить задачу")
            print("6. Экспорт в CSV")
            print("7. Импорт из CSV")
            print("8. Назад")

            choice = input("> ")
            if choice == '1':
                self.create_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                id = input('Введите id: ')
                self.edit_task(id)
            elif choice == '4':
                id = input('Введите id: ')
                self.delete_task(id)
            elif choice == '5':
                id = input('Введите id: ')
                self.done_task(id)
            elif choice == '6':
                self.export_tasks_csv()
            elif choice == '5':
                self.import_tasks_csv()
                self.save_tasks()
            elif choice == '8':
                main()
            else:
                print("Неверный выбор.")
                self.manage_tasks()
                
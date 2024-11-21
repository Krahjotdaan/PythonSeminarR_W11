from calculator import *
from note import *
from contact import *
from task import *

def main():
    note = Note()
    contact = Contact()
    task = Task()

    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Калькулятор")
        print("5. Выход")

        choice = input("> ")

        if choice == '1':
            note.manage_notes()
        elif choice == '2':
            task.manage_tasks()
        elif choice == '3':
            contact.manage_contacts()
        elif choice == '4':
            calculator()
        elif choice == '5':
             break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
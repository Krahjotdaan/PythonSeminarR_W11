def calculator():
    from personal_assistant import main

    while True:
        print("\nКалькулятор:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("> ")
        if choice == '5':
            main()

        try:
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if choice == '1':
                    result = num1 + num2
                elif choice == '2':
                    result = num1 - num2
                elif choice == '3':
                    result = num1 * num2
                elif choice == '4':
                    if num2 == 0:
                        print("Ошибка: деление на ноль!")
                        continue
                    result = num1 / num2

                print(f"Результат: {result}")
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Ошибка: {e}")

import math

def calculator():
    while True:
        try:
            print("\nВыберите операцию:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Квадратный корень")
            print("7. Факториал")
            print("8. Синус")
            print("9. Косинус")
            print("10. Тангенс")
            print("11. Выход")
            
            choice = input("Введите номер операции: ")
            
            if choice == '1':
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = num1 + num2
                print(f"Результат: {result}")
            
            elif choice == '2':
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = num1 - num2
                print(f"Результат: {result}")
            
            elif choice == '3':
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = num1 * num2
                print(f"Результат: {result}")
            
            elif choice == '4':
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = num1 / num2
                print(f"Результат: {result}")

            elif choice == '5':
                num1 = float(input("Введите число: "))
                power = float(input("Введите степень: "))
                result = math.pow(num1, power)
                print(f"Результат: {result}")
            
            elif choice == '6':
                num = float(input("Введите число: "))
                result = math.sqrt(num)
                print(f"Результат: {result}")
            
            elif choice == '7':
                num = int(input("Введите число: "))
                result = math.factorial(num)
                print(f"Результат: {result}")
            
            elif choice == '8':
                num = float(input("Введите число: "))
                result = math.sin(num)
                print(f"Результат: {result}")
            
            elif choice == '9':
                num = float(input("Введите число: "))
                result = math.cos(num)
                print(f"Результат: {result}")
            
            elif choice == '10':
                num = float(input("Введите число: "))
                result = math.tan(num)
                print(f"Результат: {result}")
            
            elif choice == '11':
                break
            
            else:
                print("Неверный выбор операции. Попробуйте снова.")
        except:
            print("error")
       


calculator()
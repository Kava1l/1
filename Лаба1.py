import random

def remove_longest_chain_of_evens(lst):
    longest_chain = []
    current_chain = []
    for num in lst:
        if num % 2 == 0:  # если число четное
            current_chain.append(num)  # добавляем его в текущую цепочку
        else:  # если число нечетное
            if len(current_chain) > len(longest_chain):  # проверяем длину текущей цепочки
                longest_chain = current_chain  # если текущая цепочка длиннее, сохраняем её как самую длинную
            current_chain = []  # сбрасываем текущую цепочку после нечетного числа
    if len(current_chain) > len(longest_chain):  # проверяем последнюю цепочку
        longest_chain = current_chain  # если последняя цепочка была самой длинной, сохраняем её
    for num in longest_chain:  # удаляем самую длинную цепочку четных чисел из списка
        lst.remove(num)
    return lst

def manual_input():
    lst = []
    while True:
        try:
            num = int(input("Введите число (0 для завершения ввода): "))
            if num == 0:
                break
            lst.append(num)
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    return lst

def auto_generation():
    lst = [random.randint(1, 10) for _ in range(random.randint(5, 10))]
    return lst

print("Выберите метод создания списка:")
print("1. Ручной ввод")
print("2. Автоматическая генерация")
choice = input("Введите номер метода: ")
if choice == "1":
    lst = manual_input()
elif choice == "2":
    lst = auto_generation()
else:
    print("Некорректный выбор метода. Завершение программы.")
    exit()

print("Исходный список:", lst)
result = remove_longest_chain_of_evens(lst)
print("Список после удаления самой длинной цепочки четных чисел:", result)

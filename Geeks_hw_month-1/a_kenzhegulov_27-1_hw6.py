# """Функция Калькулятор"""
#
# def calculator():
#     """Принимает первое число,действие и потом второе число,
#     в конце возвращает число в зависимости от выбранного действия."""
#     n1 = input('Первое число: ')
#     action = input('Действие: ')
#     n2 = input('Второе число: ')
#     if action == '+':
#         return float(n1) + float(n2)
#     elif action == '-':
#         return float(n1) - float(n2)
#     elif action == '*':
#         return float(n1) * float(n2)
#     elif action == '**':
#         return float(n1) ** float(n2)
#     elif action == '/':
#         return float(n1) / float(n2)
#     elif action == '//':
#         return float(n1) // float(n2)
#     elif action == '%':
#         return float(n1) % float(n2)
#     else:
#         print('Выберите правильное действие')
#
# print(calculator())



#
# """Функция Зеркальная строка"""
#
# def mirror(word='hello'):
#     """Если принятая строка одинаково читается в обоих направлениях - возвращает True, если нет - False."""
#     if word == word[::-1]:
#         return True
#     else:
#         return False
# print(mirror('madam'))



# """Функция Перемножение чисел"""
#
# def multiply(*args):
#     """Функция принимает неограниченное количество чисел и возвращает их перемноженную сумму."""
#     one = 1
#     for i in args:
#         one *= i
#     return one
# print(multiply(2, 3, 4, 5))
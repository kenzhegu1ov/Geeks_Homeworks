ten = [i for i in range(1, 11)]
print(ten)

evens = list(filter(lambda x: x%2 == 0, ten))
print(evens)

squared = list(map(lambda x: x**2, evens))
print(squared)

def get_from_index(index=ten):
    while True:
        try:
            num = input("введите индекс: ")
            if num == 'stop':
                break
            else:
                print(index[int(num)])
        except Exception:
            print(f"Вводить индекс только от 0 до {len(index)-1}")
get_from_index('GeekTech')


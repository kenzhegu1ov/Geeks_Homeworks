b = int(input("Температура в Баткенской области:"))

o = int(input("Температура в Ошской области:"))

n = int(input("Температура в Нарынской области:"))

j = int(input("Температура в Джалал-Абадской области:"))

t = int(input("Температура в Таласской области:"))

ch = int(input("Температура в Чуйской области области:"))

ik = int(input("Температура в Иссык-Кульской области:"))

aver_temp = round((b + o + n + j + t + ch + ik) // 7 ,2)


print(f"Средняя температура в областях КР:", (aver_temp), '°C',  )
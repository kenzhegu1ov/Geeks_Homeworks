a = input('Cлово:').lower()

glas = 0
soglas = 0
gl = 'aeoiuауоыэяюёие'
sogl = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'

for i in a:
    if i in gl:
        glas += 1
    else:
        soglas += 1
print('Количество букв:', len(a))
print('Количество гласных:', glas)
print('Количество согласных:', soglas)
print('Гласные:', round(glas/len(a)*100 , 2), '%')
print('Согласные:', round(soglas/len(a)*100 , 2), '%')

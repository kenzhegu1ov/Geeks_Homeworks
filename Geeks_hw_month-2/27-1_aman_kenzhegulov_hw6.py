import re
while True:
    print('1-Считать все имена и фамилии\n'
          '2-Считать все емейлы\n'
          '3-Считать названия файлов\n'
          '4-Считать цвета\n'
          '5-Остановить программу')
    action = int(input('Выберите действие: '))
    if action == 1:
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content = file.read()
            with open("name.txt", 'w', encoding='utf-8') as names:
                name = re.findall(r"(?:[A-Z-'][a-z-']+\s)(?:[A-Za-z'-]*\s|[A-Za-z-'])", content)
                for i in name:
                    i = str(i)
                    names.write(i + '\n')


    elif action == 2:
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as f:
            content = f.read()
            with open("email.txt", 'w', encoding='utf-8') as emails:
                email = re.findall(r"(?:[A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(?:\.[A-Z|a-z]{2,})+", content)
                for i in email:
                    i = str(i)
                    emails.write(i + '\n')

    elif action == 3:
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as s:
            content = s.read()
            with open("file names.txt", 'w', encoding='utf-8') as file_names:
                file_name = re.findall(r"\s[A-Za-z]+\.[A-Za-z0-9]+", content)
                for i in file_name:
                    i = str(i)
                    file_names.write(i + '\n')


    elif action == 4:
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as s:
            content = s.read()
            with open("colors.txt", 'w', encoding='utf-8') as colors:
                color = re.findall(r"#[a-z0-9]+", content)
                for i in color:
                    i = str(i)
                    colors.write(i + '\n')


    elif action == 5:
        print('Программа остановлена')
        break


    else:
        print('Только цифры от 1 до 5')
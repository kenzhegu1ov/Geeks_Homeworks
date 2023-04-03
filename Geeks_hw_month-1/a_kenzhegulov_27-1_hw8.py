with open("results.txt", "r", encoding='UTF-8') as f:
    print(f.read())
students = {}
with open("results.txt", encoding='UTF-8') as file:
    onstring = file.read().split("\n")[:-1]
for item in onstring:
    key = item.split()[1]
    value = item.split(" ")[-1]
    students[key] = value
file.close()
sort = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
#print(sort)
top = dict(list(sort.items())[:3])
with open("sorted_results.txt", "w", encoding='UTF-8') as f:
    for i in sort, top:
        f.write(f"{i}\n")

with open("sorted_results.txt", "r", encoding = "UTF-8") as result:
    print(result.read())
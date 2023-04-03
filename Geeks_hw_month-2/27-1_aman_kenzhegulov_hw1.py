class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married


    def introduce_myself(self):

        return (f'Full name: {self.fullname}\n'
                f'Age: {self.age}\n' 
                f'Married: {self.is_married}')
aman = Person('Aman', 17, 'No')
print(aman.introduce_myself())


print('=' * 100)


class Teacher(Person):
    salary = 25000
    def __init__(self,fullname, age, is_married,experience):
        super().__init__(fullname, age, is_married)
        self.experiences = experience


    def calculation(self):
        if self.experiences > 3:
            new_salary = self.salary + self.salary*(0.05*(self.experiences-3))
            return new_salary
        else:
            return self.salary


    def introduce_myself(self):

        return (f'Full name: {self.fullname}\n'
                f'Age: {self.age}\n'
                f'Married: {self.is_married}\n'
                f'Exp: {self.experiences}\n'
                f'Salary: {self.calculation()}')
Teacher_1 = Teacher('Amanbek uulu Daniyar', 20, 'no', 4)
print(Teacher_1.introduce_myself())


print('=' * 100)


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def introduce_myself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} \n'
                f'{self.marks}')

    def avg_rating(self):
        return int(sum(self.marks.values()) / len(self.marks))

def create_students():
    student_1 = Student(fullname='Akzhol', age=17, is_married='No', marks=
                        {'Math': 4, 'English': 3, 'Russian': 5, 'physics': 3})
    student_2 = Student(fullname='Salymbek', age=17, is_married='No', marks=
                        {'Math': 4, 'English': 5, 'Russian': 4, 'physics': 5})
    student_3 = Student(fullname='Daniel', age=17, is_married='No', marks=
                        {'Math': 4, 'English': 5, 'Russian': 5, 'Physics': 4})
    list_of_Students = [student_1, student_2, student_3]
    return list_of_Students

students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f'Name: {i.fullname}\n'
        f'Age: {i.age}\n'
        f'Maried: {i.is_married}\n'
        f'Math: {list[0]}\n'
        f'English: {list[1]}\n' 
        f'Russian: {list[2]}\n'
        f'Physics: {list[3]}\n'
        f"Average marks: {sum(list)/len(list)}\n")


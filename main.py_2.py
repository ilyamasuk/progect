#ООП. ВСТУП
class Student:
    count_of_student = 0

    def say_hi(self):
        print(f'Hi! I` m {self.name}')

    def __init__(self, name, height): #Цей метод спрацьовує при ініцінілізація екземпляра
        self.name = name
        self.height = height
        Student.count_of_student += 1

    def __del__(self):
        print('Bay')

    def __str__(self):
        return  self.name


sergiy = Student('sergiy', 180)
anton = Student('anton', 160)

sergiy.say_hi()
anton.say_hi()

print(sergiy.height)
print(anton.height)
print(Student.count_of_student)
print(anton)
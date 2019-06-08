class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' ' + str(self.age)



if __name__ == '__main__':
    student = Student('yijun', 10)
    print(student)

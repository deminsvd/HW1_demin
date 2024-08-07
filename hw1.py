class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
            or course in self.finished_courses and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def ever_rate(self):
        list_hwvalues = []
        for hw_value in self.grades.values():
            list_hwvalues += hw_value
        return sum(list_hwvalues)/len(list_hwvalues)
    def __str__(self):

        return ('\nИмя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя'
                ' оценка за домашние задания: ' + str(self.ever_rate()) +
                '\nКурсы в процессе изучения: ' + ', '.join(str(el) for el in self.courses_in_progress) +
                '\nЗавершенные курсы: ' + ', '.join(str(el) for el in self.finished_courses))

    def __lt__(self, student):
        if isinstance (student, Student):
            if self.ever_rate() < student.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не студент. Сравните, пожалуйста, студентов'

    def __le__(self, student):
        if isinstance (student, Student):
            if self.ever_rate() <= student.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не студент. Сравните, пожалуйста, студентов'

    def __eq__(self, student):
        if isinstance (student, Student):
            if self.ever_rate() == student.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не студент. Сравните, пожалуйста, студентов'

    def __ne__(self, student):
        if isinstance (student, Student):
            if self.ever_rate() != student.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не студент. Сравните, пожалуйста, студентов'

    def __gt__(self, student):
        if isinstance (student, Student):
            if self.ever_rate() > student.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не студент. Сравните, пожалуйста, студентов'

    def __ge__(self, student):
        if isinstance (student, Student):
            if self.ever_rate() >= student.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не студент. Сравните, пожалуйста, студентов'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def ever_rate(self):
        list_rates = []
        for lec_value in self.grades.values():
            list_rates += lec_value
        return sum(list_rates)/len(list_rates)

    def __str__(self):

        return ('\nИмя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя' 
                ' оценка за лекции: ' + str(self.ever_rate()))

    def __lt__(self, lecturer):
        if isinstance (lecturer, Lecturer):
            if self.ever_rate() < lecturer.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не лектор. Сравните, пожалуйста, лекторов'

    def __le__(self, lecturer):
        if isinstance (lecturer, Lecturer):
            if self.ever_rate() <= lecturer.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не лектор. Сравните, пожалуйста, лекторов'

    def __eq__(self, lecturer):
        if isinstance (lecturer, Lecturer):
            if self.ever_rate() == lecturer.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не лектор. Сравните, пожалуйста, лекторов'

    def __ne__(self, lecturer):
        if isinstance (lecturer, Lecturer):
            if self.ever_rate() != lecturer.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не лектор. Сравните, пожалуйста, лекторов'

    def __gt__(self, lecturer):
        if isinstance (lecturer, Lecturer):
            if self.ever_rate() > lecturer.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не лектор. Сравните, пожалуйста, лекторов'

    def __ge__(self, lecturer):
        if isinstance (lecturer, Lecturer):
            if self.ever_rate() >= lecturer.ever_rate():
                return True
            else:
                return False
        else:
            return 'Один из аргументов не лектор. Сравните, пожалуйста, лекторов'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return '\nИмя: ' + self.name + '\nФамилия: ' + self.surname

def course_everagerate(list_student,course_title):
    rate_list = []
    for each_student in list_student:
        if isinstance(each_student, Student) and each_student.grades.get(course_title) is not None:
            rate_list += each_student.grades.get(course_title)
    return f'Cредняя оценка за домашние задания по всем студентам в рамках курса {course_title}: ' + str(sum(rate_list)/len(rate_list))

def course_lec_everagerate(list_lecturer, course_title):
    rate_list = []
    for each_lecturer in list_lecturer:
        if isinstance(each_lecturer, Lecturer) and each_lecturer.grades.get(course_title) is not None:
            rate_list += each_lecturer.grades.get(course_title)
    return f'Cредняя оценка за лекции всех лекторов в рамках курса {course_title}: ' + str(
        sum(rate_list) / len(rate_list))


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Some', 'Student', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Reviewer')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']


cool_lecturer = Lecturer('Some', 'Lecturer')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']


best_lecturer = Lecturer('Some', 'Lecturer')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Git', 10)

cool_reviewer.rate_hw(some_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 7)

best_student.rate_lec(cool_lecturer, 'Python', 8)
some_student.rate_lec(cool_lecturer, 'Python', 7)
some_student.rate_lec(cool_lecturer, 'Git', 10)


best_student.rate_lec(best_lecturer, 'Python', 10)
some_student.rate_lec(best_lecturer, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)

print(some_student<best_student)
print(best_student<some_student)
print(some_student<cool_reviewer)

print(some_student<=best_student)
print(best_student<=some_student)
print(some_student<=cool_reviewer)

print(best_student==best_student)
print(best_student==some_student)
print(some_student==cool_reviewer)

print(best_student!=some_student)
print(best_student!=best_student)
print(some_student!=cool_reviewer)

print(some_student>best_student)
print(best_student>some_student)
print(some_student>cool_reviewer)

print(some_student>=best_student)
print(best_student>=some_student)
print(some_student>=cool_reviewer)

print(cool_lecturer<best_lecturer)
print(best_lecturer<cool_lecturer)
print(cool_lecturer<cool_reviewer)

print(cool_lecturer<=best_lecturer)
print(best_lecturer<=cool_lecturer)
print(cool_lecturer<=cool_reviewer)

print(best_lecturer==best_lecturer)
print(best_lecturer==cool_lecturer)
print(cool_lecturer==cool_reviewer)

print(best_lecturer!=best_lecturer)
print(best_lecturer!=cool_lecturer)
print(cool_lecturer!=cool_reviewer)

print(cool_lecturer>best_lecturer)
print(best_lecturer>cool_lecturer)
print(cool_lecturer>cool_reviewer)

print(best_lecturer>=cool_lecturer)
print(cool_lecturer>=best_lecturer)
print(cool_lecturer>=cool_reviewer)

print()
student_list = [best_student,some_student]
print(course_everagerate(student_list,'Python'))

print()
lecturer_list = [cool_lecturer,best_lecturer]
print(course_lec_everagerate(lecturer_list,'Git'))
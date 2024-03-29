# Задание №2 Атрибуты и взаимодействие классов

class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      self.courses_attached = []

  def rate_lct(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

#TASK_1            
class Lecturer(Mentor):
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.courses_attached = []
    self.grades = {}
    self.courses_in_progress = []

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
#TASK_2
best_lecturer = Lecturer('Some', 'One', 'your_gender')
best_lecturer.courses_in_progress += ['Python']

cool_student = Student('Some', 'Body', 'your_gender')
cool_student.courses_attached += ['Python']

cool_student.rate_lct(best_lecturer, 'Python', 10)
cool_student.rate_lct(best_lecturer, 'Python', 10)
cool_student.rate_lct(best_lecturer, 'Python', 10)


print(best_student.grades)
print(best_lecturer.grades)
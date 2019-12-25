
class disc_golf_course:
    var1 = "Gentlemen, start your engines"

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

class Student:
    class_count = 0

    def __init__(self, name):
        self.student_id = Student.class_count + 1
        self.name = name
        Student.class_count += 1

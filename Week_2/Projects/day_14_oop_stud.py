class Students:
    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks

        def get_name(self):
            return self.name
        
        def get_marks(self):
            return self.marks
        
        def set_marks(self, umarks):
            self.marks = umarks

    students = [Student("Alice", 85),
                Student("Bob", 72),
                Student("Charlie", 90),
                Student("Diana", 66),
                Student("Ethan", 78),
                Student("Fiona", 92),
                Student("George", 59),
                Student("Hannah", 88),
                Student("Ian", 74),
                Student("Julia", 95)]

    def get_studs(self):
        return self.students
    
    def view_studs(self):
        for i in self.students:
            print(i.get_name(), ':', i.get_marks())

    def add_student(self, name, marks):
        self.students.append(self.Student(name, marks))
        print("Student added successfully")

    def update_stud_marks(self, name, marks):
        for i in self.students:
            if i.get_name() == name:
                i.set_marks(marks)
                break

    def delete_stud(self, name):
        for i in self.students:
            if i.get_name() == name:
                self.students.remove(i)
                break

studs = Students()
studs.add_student('bvns', 98)
studs.view_studs()
print('-----------------------------')
studs.add_student('PB', 100)
studs.view_studs()
print('-----------------------------')
studs.delete_stud('bvns')
studs.view_studs()
print('---------------------------')

studs.update_stud_marks('PB', 90)
studs.view_studs()
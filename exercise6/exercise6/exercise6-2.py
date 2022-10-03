class Student:

    def initialize(self, name, note):
        self.name = name
        self.note = note

    def print(self):
        print("Name: ", self.name)
        print("Note: ", self.note)

    def result(self):
        if self.note <= 5:
            print("The student has failed")
        else:
            print("The student has passed")


student1 = Student()
student2 = Student()
student3 = Student()

student1.initialize("Pabel Hernandez", 9)
student2.initialize("David Ivon", 5)
student3.initialize("Ricardo Mopevo", 3)


student1.print()
student1.result()
student2.print()
student2.result()
student3.print()
student3.result()
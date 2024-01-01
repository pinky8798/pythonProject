#Class should always have a naming convention starting with capital letter

class Student():
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def name(self):
        print(input("name: "))
    def standard(self):
        print(input("standard: "))
'''
student1=Student()
student1.email='123@gmail.com'
student1.name()
student1.standard()
print(f"Email: {student1.email}")
'''
#constructor with arguments
student2=Student('Ais','456@gmail.com')
print(student2.email)
# we can reassign the values passed through arguments to a constructor , for eg : Below we have reassigned the name of student2 object from "ais" to "Aishwarya"
student2.name='Aishwarya'
print(student2.name)
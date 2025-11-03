class Employee :
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
obj1 = Employee("Anandhu", "Trainer")
obj1.display()

class Trainer (Employee):
    def __init__(self, name, role,specialization):
        Employee.__init__(self,name, role)
        self.specialization = specialization
    def display(self):
         Employee.display(self)
         print("specialization:", self.specialization)
obj2 = Trainer("Mridula", "Senior Trainer", "Cardio")
obj2.display()

class YogaInstructor(Employee):
    def __init__(self,name,role,yoga_style):
         Employee.__init__(self,name,role)
         self.yoga_style = yoga_style
    def display(self):
        Employee.display(self)
        print("yoga_style:",self.yoga_style)
obj3 = YogaInstructor("Arun", "Instructor", "Hatha Yoga")
obj3.display()

class MultiTrainer(Trainer,YogaInstructor):
     def __init__(self,name,role,specialization,yoga_style):
            super().__init__(name,role,specialization)
            self.yoga_style = yoga_style
     def display(self):
            super().display()
            print("yoga_style:",self.yoga_style)
obj4 = MultiTrainer("Arjun", "Lead Trainer", "Strength Training", "Vinyasa Yoga")
obj4.display()    

# A fitness center wants to create a simple system to define and display staff profiles based on their roles for record-keeping purposes. You are tasked with creating a Python program to represent different types of staff. Complete the following steps:

# Define a base class Employee with attributes name (string) and role (string), and a method display() that prints the employee’s name and role.
# Create a class Trainer that inherits from Employee, adds an attribute specialization (string), and includes a display() method to print the trainer’s name, role, and specialization.
# Create a class YogaInstructor that inherits from Employee, adds an attribute yoga_style (string), and includes a display() method to print the yoga instructor’s name, role, and yoga style.
# Create a class MultiTrainer that inherits from both Trainer and YogaInstructor, includes both specialization and yoga_style attributes, and has a display() method to print the multi-trainer’s name, role, specialization, and yoga style.
# Create one object from each class (Employee, Trainer, YogaInstructor, MultiTrainer) with sample data.
# Display the details of each object by calling its display() method
        
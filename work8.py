class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_details(self):
        print("name:",self.name)
        print("age:",self.age)

obj1 = person("reshma",23)
obj1.show_details()

print("--------------employee class-------")
class employee(person):
    def __init__(self, name, age,employee_id):
        person.__init__(self,name, age)
        self.employee_id = employee_id
    def show_details(self):
        person.show_details(self)
        print("employee_id:",self.employee_id)  
        
         
obj2 = employee("Sneha", 28, 101) 
obj2.show_details()
print("--------------parttime class-------")

class parttime(person):
    def __init__(self,name, age,working_hours):
        person.__init__(self,name,age)
        self.working_hours = working_hours
    def show_details(self):
        person.show_details(self)
        print("working_hours:",self.working_hours)
obj3 = parttime("Megha", 22, 6)
obj3.show_details()
print("-----consultant class-------")
class consultant(employee,parttime):
    def __init__(self,name, age,employee_id,working_hours,project_name):
        super().__init__(name,age,employee_id)
        self.working_hours = working_hours
        self.project_name = project_name
    def show_details(self):
        super().show_details()
        print("project_name",self.project_name) 
        print("working_hours",self.working_hours)         
obj4 = consultant("Abhi", 30, 102, 5,"AI Project")
obj4.show_details()


# A company wants to create a simple system to define and display employee profiles based on their role types for record-keeping purposes. You are tasked with creating classes to represent different types of individuals in Python. Complete the following steps:

# Create a class Person with attributes name (string) and age (integer), and a method show_details() that prints the person’s name and age.
# Create a class Employee that inherits from Person, adds an attribute employee_id (string), and includes a show_details() method to print the employee’s name, age, and employee ID.
# Create a class PartTime that inherits from Person, adds an attribute working_hours (float), and includes a show_details() method to print the part-time worker’s name, age, and working hours.
# Create a class Consultant that inherits from both Employee and PartTime, adds an attribute project_name (string), and includes a show_details() method to print the consultant’s name, age, employee ID, working hours, and project name.
# Create one object of each class (Person, Employee, PartTime, Consultant) with sample data.
# Display the details of each object by calling its show_details() method

       
   

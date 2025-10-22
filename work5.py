python = {"Megha","Sneha","Abhi","Ansi","Misa"}
data_science = {"Misa","Aishu","Alna","Sree"}
python.add("Libi")
data_science.remove("Sree")
print("students in both courses:",python & data_science)
print("students only in python:",python-data_science)
print("all students in either course:",python.union(data_science))
students = {
    "python": len(python),
    "data_science": len(data_science)
    }

for x, y in students.items():
  print(f"course:{x} , students:{y}")

growth = {x: y*2 for x,y in students.items()}
print("Expected growth (doubled values):",growth)

# you are creating a basic system to manage students enrolled in various courses.
# Create two sets: one for students enrolled in "Python" and one for "Data Science".
# Add a new student to the Python set.
# Remove one student from the Data Science set.
# Find and display the names of students who are enrolled in both courses.
# Find students who are only in the Python course but not in Data Science.
# Display the combined list of all students in either course (no duplicates).
# Create a dictionary with course names as keys and number of students as values.
# Using a loop, print the course name and number of students in the format:
# Course: Python, Students: 3
# Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled (to simulate expected growth)



  
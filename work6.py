attendance = [18, 20, 19, 15, 21]
total_attendance = 0
total_count = 0

for students in attendance:
    total_attendance += students
    if students >= 20:
        print("full")
        total_count += 1
    else:
        print("not full")
print("total_attendance:",total_attendance)
print("total_count:",total_count)

# You are working on a simple attendance tracking system for a 5-day workshop. You have a list of the number of students present each day:
# attendance = [18, 20, 19, 15, 21]
# Your tasks are:
# Loop through the list and print whether the class was "Full" if 20 or more students were present, or "Not Full" otherwise.
# Count how many days the class was full.
# Calculate and print the total attendance for all 5 days.





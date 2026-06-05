total_students = 30

present_count = 0
absent_count = 0

for i in range(1, total_students + 1):
    attendance = input(f"Student {i} Attendance (Present/Absent): ").strip().lower()

    if attendance == "present":
        present_count += 1
    elif attendance == "absent":
        absent_count += 1
    else:
        print("Invalid input! Counting as Absent.")
        absent_count += 1

print("\n--- Attendance Summary ---")
print("No. of Students Present:", present_count)
print("No. of Students Absent:", absent_count)

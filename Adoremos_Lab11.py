grades = []
passed_students = 0
total_students = 0

# Loop to input grades for any number of students
while True:
    user_input = input("Enter a grade for a student: ")

    # Check if user wants to stop
    if user_input == 'done':
        print("Exiting the grade entry process.")
        break

    # Try to convert the input to an integer (grade)
    try:
        grade = int(user_input)

        # Check if the grade is within the valid range
        if 40 <= grade <= 100:
            grades.append(grade)
            total_students += 1

            # Check if the student has passed
            if grade >= 50:
                passed_students += 1
        else:
            print("Invalid grade.")
            break
    except ValueError:
        print("Error. Please enter a number between 40 to 100, or 'done' to stop.")

# Calculate the average grade and passing percentage
if grades:
    average_grade = sum(grades) / len(grades)
    passing = (passed_students / total_students) * 100 if total_students > 0 else 0

    #results
    print(f"\nGrades entered: {grades}")
    print(f"Average grade: {average_grade:.2f}")
    print(f"Number of students who passed: {passed_students}")
    print(f"Passing percentage: {passing:.2f}%")
else:
    print("\nNo valid grades were entered.")

 
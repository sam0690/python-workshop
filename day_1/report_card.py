def get_student_data():
    """Gets student name, number of subjects, and marks for each subject."""
    student_name = input("Enter the student's name: ")
    num_subjects = int(input("Enter the number of subjects: "))
    
    subjects = {}
    for i in range(num_subjects):
        subject_name = input(f"Enter the name of subject #{i + 1}: ")
        marks = float(input(f"Enter marks for {subject_name} (out of 100): "))
        subjects[subject_name] = marks
    
    return student_name, subjects

def calculate_results(subjects):
    """Calculates total, average, and grade from the subjects dictionary."""
    total_marks = sum(subjects.values())
    average_marks = total_marks / len(subjects)
    
    if average_marks >= 90:
        grade = "A+"
    elif average_marks >= 80:
        grade = "A"
    elif average_marks >= 70:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    else:
        grade = "Fail"
    
    return total_marks, average_marks, grade

def print_report_card(student_name, subjects, total, average, grade):
    """Prints a formatted report card."""
    print("\n----- Report Card for", student_name, "-----")
    print("Subjects:")
    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")
    print(f"\nTotal Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
    print("-------------------------------")

# Main program
def main():
    student_name, subjects = get_student_data()
    total, average, grade = calculate_results(subjects)
    print_report_card(student_name, subjects, total, average, grade)

if __name__ == "__main__":
    main()

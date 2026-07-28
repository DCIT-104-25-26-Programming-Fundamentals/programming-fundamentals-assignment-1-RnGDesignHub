# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def display_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def calculate_average(scores):
    total = 0

    for score in scores:
        total = total + score

    return total / len(scores)


def add_student(students):
    name = input("Student name: ")

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    for student in students:
        if student["id"] == student_id:
            print("Error: That student ID already exists.")
            return

    try:
        number_of_scores = int(input("How many scores? "))
    except ValueError:
        print("Error: Please enter a valid number of scores.")
        return

    if number_of_scores <= 0:
        print("Error: Number of scores must be positive.")
        return

    scores = []

    for i in range(number_of_scores):
        try:
            score = float(input(f"Enter score {i + 1}: "))
        except ValueError:
            print("Error: Scores must be numbers.")
            return

        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    if len(students) == 0:
        print("No student records have been added.")
        return

    print("-" * 65)
    print(f"{'Name':<18}{'ID':<12}{'Scores':<25}{'Average'}")
    print("-" * 65)

    for student in students:
        score_text = ""

        for i in range(len(student["scores"])):
            score = student["scores"][i]

            if score.is_integer():
                score_text = score_text + str(int(score))
            else:
                score_text = score_text + str(score)

            if i < len(student["scores"]) - 1:
                score_text = score_text + ", "

        average = calculate_average(student["scores"])
        print(
            f"{student['name']:<18}"
            f"{student['id']:<12}"
            f"{score_text:<25}"
            f"{average:.2f}"
        )

    print("-" * 65)


def calculate_student_average(students):
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Error: Student ID not found.")


def quit_program():
    print("Goodbye!")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            quit_program()
            break
        else:
            print("Error: Please enter a choice from 1 to 4.")


if __name__ == "__main__":
    main()

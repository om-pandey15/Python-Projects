#Initialising dictionary(key+value)

student_grade = {}

#Add a new student
def add_student(name, grade):
    student_grade[name] = grade
    #[om]= 100
    print(f"Added: {name} with a Grade: {grade}")
    #Added om with a Grade: 100

#Update a student's grade
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        #Om= 200
        print(f"Updated: {name} with a Grade: {grade}")
    else:
        print(f"Student {name} not found.")

#Delete a student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"Deleted: {name}")
    else:
        print(f"Student {name} not found.")

#View all student
def display_all_students():
    if student_grade:
        print("All Students and Grades:")
        for name, grade in student_grade.items():#(.items()= displays all key-value pairs)
            print(f"  {name}: {grade}")
    else:
        print("No students found.")

#Main function to demonstrate the functionality
def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)

        elif choice == "2":
            name = input("Enter student name: ")
            grade = int(input("Enter new grade: "))
            update_student(name, grade)

        elif choice == "3":
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == "4":
            display_all_students()

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        if __name__ == "__main__":
            main()
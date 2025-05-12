import db

def show_menu():
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def add_student_ui():
    print("\n--- Add Student ---")
    name = input("Name: ")
    roll = input("Roll No: ")
    dept = input("Department: ")
    year = input("Year: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    try:
        db.add_student(name, roll, dept, year, email, phone)
        print("✅ Student added successfully!")
    except Exception as e:
        print("❌ Error adding student:", e)

def view_all_students():
    print("\n--- All Students ---")
    students = db.list_students()
    
    if students:
        for student in students:
            print(f"Name: {student[1]}, Roll No: {student[2]}, Department: {student[3]}, Year: {student[4]}, Email: {student[5]}, Phone: {student[6]}, Last Updated: {student[7]}")
    else:
        print("❌ No students found.")

def search_student():
    print("\n--- Search Student by Roll No ---")
    roll = input("Enter Roll No: ")
    student = db.find_student_by_roll(roll)
    
    if student:
        print(f"Name: {student[1]}, Roll No: {student[2]}, Department: {student[3]}, Year: {student[4]}, Email: {student[5]}, Phone: {student[6]}, Last Updated: {student[7]}")
    else:
        print("❌ No student found with that roll number.")

def update_student_ui():
    print("\n--- Update Student ---")
    roll = input("Enter Roll No to update: ")
    
    student = db.find_student_by_roll(roll)
    if student:
        print("Current details:")
        print(f"Name: {student[1]}, Department: {student[3]}, Year: {student[4]}, Email: {student[5]}, Phone: {student[6]}")
        
        # Ask for new details
        name = input("New Name (leave blank to keep current): ") or student[1]
        dept = input("New Department (leave blank to keep current): ") or student[3]
        year = input("New Year (leave blank to keep current): ") or student[4]
        email = input("New Email (leave blank to keep current): ") or student[5]
        phone = input("New Phone (leave blank to keep current): ") or student[6]
        
        db.update_student(roll, name, dept, year, email, phone)
        print("✅ Student updated successfully!")
    else:
        print("❌ No student found with that roll number.")

def delete_student_ui():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll No to delete: ")
    
    student = db.find_student_by_roll(roll)
    if student:
        confirm = input(f"Are you sure you want to delete student {student[1]}? (y/n): ").lower()
        if confirm == 'y':
            db.remove_student(roll)
            print("✅ Student deleted successfully!")
        else:
            print("❌ Deletion canceled.")
    else:
        print("❌ No student found with that roll number.")

def main():
    db.init_db()  # Ensure database and table are ready
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student_ui()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student_ui()
        elif choice == '5':
            delete_student_ui()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# ✅ Make sure this is at the bottom of the file:
if __name__ == "__main__":
    main()

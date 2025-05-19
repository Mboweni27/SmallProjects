import sqlite3

def display_menu():
    print("\nStudent Database Menu")
    print("1. Create Table student")
    print("2. Add new student(s)")
    print("3. View Table")
    print("4. PLACEHOLDER")
    print("5. PLACEHOLDER")
    print("6. Drop Table student")
    print("7. Exit")

def create_table():
    try:
        connect = sqlite3.connect("Student.db")
        cursor = connect.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS students (
                       student_id INTEGER PRIMARY KEY,
                       f_name TEXT,
                       l_name TEXT,
                       avg_mark REAL
                       )
                       """
                       )
        connect.commit()
        connect.close()
        print("Table 'STUDENTS' has been created or already existed.")
    except Exception as e:
        print("An error has occured: ", e)

def add_student():
    try: 
        with sqlite3.connect("Student.db") as conn:
            cursor = conn.cursor()
            while True:
                f_name = input("Enter first name: ")
                l_name = input("Enter last name: ")
                try:
                    avg_mark = float(input("Enter your average mark: "))
                except Exception as e:
                    print("There was a problem with your average mark")
                    continue
                insert = "INSERT INTO students (f_name, l_name, avg_mark) VALUES (?, ?, ?)"
                cursor.execute(insert, (f_name, l_name, avg_mark))
                print("Student Added: ", f_name,l_name, "Mark:", avg_mark)
                another_input = input("Do you want to add another student record? (y/n): ")
                if another_input.lower() != 'y':
                    break
        print("Student input complete!") 
    except Exception as e:
        print("Error inserting data: ", e)

def drop_table():
    usure = input("Are you sure you want to delete this table?(y/n): ")     
    if usure.lower() != 'n':
        try:
            with sqlite3.connect("Student.db") as conn:
                cursor = conn.cursor()
                cursor.execute("DROP TABLE IF EXISTS students")
                print("Table has been deleted!")
        except Exception as e:
            print("Failed to delete the table: ", e)
    else:
        print("Table was not deleted")

def view_db():
    try:
        with sqlite3.connect("Student.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()
            print("\n📊 DataBase")
            print("{:<5} {:<15} {:<15} {:<10}".format("ID", "Name", "Surname", "Average"))

            for r in records:
                print("{:<5} {:<15} {:<15} {:<10.2f}".format(r[0], r[1], r[2], r[3]))
    except Exception as e:
        print("There exists no database to view!")

def main():

    user_option = ""

    while user_option != "7":

        display_menu()
        user_option = input("Choose an option: ")

        if user_option == "1":
            create_table()
            pass
        elif user_option == "2":
            add_student()
            pass
        elif user_option == "3":
            view_db()
        elif user_option in {"4", "5"}:
            print("This feature is not yet implemented.")
        elif user_option == "6":
            drop_table()
            pass
        elif user_option == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

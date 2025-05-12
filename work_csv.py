import csv
import db

def import_students_from_csv(csv_file):
    db.init_db()
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            try:
                db.add_student(
                    row['Name'],
                    row['Roll No'],
                    row['Department'],
                    row['Year'],
                    row['Email'],
                    row['Phone']
                )
                count += 1
            except Exception as e:
                print(f"❌ Failed to add {row['Roll No']}: {e}")
        print(f"\n✅ Successfully imported {count} students.")

if __name__ == "__main__":
    import_students_from_csv("indian_students_dataset.csv")

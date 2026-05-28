import json
import csv

class EmployeeManager:
    def __init__(self, csvpath, jsonpath):
        self.csvpath = csvpath
        self.jsonpath = jsonpath

    # ---------------- JSON Handling ----------------
    def get_json_data(self):
        try:
            with open(self.jsonpath) as jsonfile:
                return json.load(jsonfile)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON file.")
            return []

    def save_json(self, data):
        try:
            with open(self.jsonpath, "w") as f:
                json.dump(data, f, indent=4)
            print("Data saved to JSON successfully!")
        except Exception as e:
            print("Error saving JSON:", e)

    # ---------------- CSV Handling ----------------
    def get_csv_data(self):
        try:
            with open(self.csvpath, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader), reader.fieldnames
        except FileNotFoundError:
            return [], ['name', 'department', 'salary']

    def export_csv(self):
        data = self.get_json_data()
        fields = ["name", "department", "salary"]
        try:
            with open(self.csvpath, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)
            print("Data exported to CSV successfully!")
        except Exception as e:
            print("Error exporting CSV:", e)

    # ---------------- Employee Operations ----------------
    def add_employee(self, name, dept, salary):
        emp = {"name": name, "department": dept, "salary": salary}
        data = self.get_json_data()
        data.append(emp)
        self.save_json(data)
        print("Employee added successfully!")

    def view_employees(self):
        data = self.get_json_data()
        if not data:
            print("No employees found.")
            return
        for emp in data:
            print(f"Emp name: {emp['name']} - Dept: {emp['department']} - Salary: {emp['salary']}")

    def search_employee(self, name):
        data = self.get_json_data()
        for emp in data:
            if emp["name"].lower() == name.lower():
                print("Employee found:", emp)
                return emp
        print("Employee not found.")
        return None


# ---------------- Menu Loop ----------------
def main():
    csvpath = r"D:\Python Automation Journey\Week_3\Projects\files\employees.csv"
    jsonpath = r"D:\Python Automation Journey\Week_3\Projects\files\employees.json"

    manager = EmployeeManager(csvpath, jsonpath)

    while True:
        print("\n--- Employee Data Manager ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Save to JSON")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            dept = input("Enter department: ")
            try:
                salary = int(input("Enter salary: "))
            except ValueError:
                print("Invalid salary input.")
                continue
            manager.add_employee(name, dept, salary)

        elif choice == "2":
            manager.view_employees()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_employee(name)

        elif choice == "4":
            data = manager.get_json_data()
            manager.save_json(data)

        elif choice == "5":
            manager.export_csv()

        elif choice == "6":
            print("Exiting Employee Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

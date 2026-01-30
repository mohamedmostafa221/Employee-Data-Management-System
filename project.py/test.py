import csv

class StaffSystem:

    def __init__(self):
        self.file = "employees.csv"
        self.data = {}
        self.read_file()

    # read old employees if file exists
    def read_file(self):
        try:
            f = open(self.file, "r")
        except:
            return

        reader = csv.reader(f)
        try:
            next(reader)
        except:
            pass

        for row in reader:
            if len(row) < 5:
                continue
            self.data[row[0]] = {
                "name": row[1],
                "position": row[2],
                "salary": row[3],
                "email": row[4]
            }

        f.close()

    # save all data to csv file
    def save_file(self):
        f = open(self.file, "w", newline="")
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Position", "Salary", "Email"])

        for i in self.data:
            emp = self.data[i]
            writer.writerow([
                i,
                emp["name"],
                emp["position"],
                emp["salary"],
                emp["email"]
            ])

        f.close()

    # add new employee
    def add_employee(self):
        i = input("Enter ID: ")

        if i in self.data:
            print("ID already exists")
            return

        name = input("Enter name: ")
        position = input("Enter position: ")

        salary = input("Enter salary: ")
        if not salary.isdigit():
            print("Salary must be number")
            return

        email = input("Enter email: ")

        self.data[i] = {
            "name": name,
            "position": position,
            "salary": salary,
            "email": email
        }

        self.save_file()
        print("Employee added")

    # view all employees
    def view_all(self):
        if not self.data:
            print("No employees found")
            return

        for i in self.data:
            emp = self.data[i]
            print("-----------------------")
            print("ID:", i)
            print("Name:", emp["name"])
            print("Position:", emp["position"])
            print("Salary:", emp["salary"])
            print("Email:", emp["email"])

    # search employee by id
    def search_employee(self):
        i = input("Enter ID to search: ")

        if i not in self.data:
            print("Employee not found")
            return

        emp = self.data[i]
        print("Name:", emp["name"])
        print("Position:", emp["position"])
        print("Salary:", emp["salary"])
        print("Email:", emp["email"])

    # update employee data
    def update_employee(self):
        i = input("Enter ID to update: ")

        if i not in self.data:
            print("Employee not found")
            return

        emp = self.data[i]

        name = input("New name (leave empty to keep old): ")
        position = input("New position (leave empty to keep old): ")
        salary = input("New salary (leave empty to keep old): ")
        email = input("New email (leave empty to keep old): ")

        if name != "":
            emp["name"] = name

        if position != "":
            emp["position"] = position

        if salary != "":
            if not salary.isdigit():
                print("Invalid salary")
                return
            emp["salary"] = salary

        if email != "":
            emp["email"] = email

        self.save_file()
        print("Employee updated")

    # delete employee
    def delete_employee(self):
        i = input("Enter ID to delete: ")

        if i not in self.data:
            print("Employee not found")
            return

        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() != "y":
            return

        del self.data[i]
        self.save_file()
        print("Employee deleted")

    # menu
    def menu(self):
        while True:
            print("\n1- Add Employee")
            print("2- View All Employees")
            print("3- Update Employee")
            print("4- Delete Employee")
            print("5- Search Employee")
            print("6- Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.search_employee()
            elif choice == "6":
                print("Program closed")
                break
            else:
                print("Wrong choice")


app = StaffSystem()
app.menu()

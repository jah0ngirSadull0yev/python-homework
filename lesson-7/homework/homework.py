import os
from collections.abc import Callable

# Generalized Vector Class:

class VectorException(Exception):
    pass

class DifferentDimensionsException(VectorException):
    pass

class Vector:

    def __init__(self, *args):
        self.point = tuple(args) # immutable
        self.dimension = len(args)

    def __str__(self):
        return f"Vector{self.point}"

    def __add__(self, other: Vector):
        if self.dimension == other.dimension:
            return Vector(*[i+j for i, j in zip(self.point, other.point)])
        else:
            raise DifferentDimensionsException("Vectors must have the same dimension")
    
    def __sub__(self, other: Vector):
        if self.dimension == other.dimension:
            return Vector(*[i-j for i, j in zip(self.point, other.point)])
        else:
            raise DifferentDimensionsException("Vectors must have the same dimension")
    
    def __mul__(self, other): # Vector / number
        if isinstance(other, Vector):
            if self.dimension == other.dimension:
                return sum(i*j for i, j in zip(self.point, other.point))
            else:
                raise DifferentDimensionsException("Vectors must have the same dimension")
        return Vector(*[i*other for i in self.point])
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def magnitude(self):
        return sum(i**2 for i in self.point)**0.5
    
    def normalize(self):
        return self.__mul__(1 / self.magnitude())
    




# Employee Records Manager:

class Employee:

    def __init__(self, employee_id: int, name: str, position: str, salary: int):
        self.employee_id: int = employee_id
        self.name: str = name
        self.position: str = position
        self.salary: int = salary

    def __str__(self):
        return f"Employee({self.employee_id}, {self.name}, {self.position}, {self.salary})"
    
    def row(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:

    def __init__(self, db: str = "employees.txt"):
        self.db: str = db
        self.data: list[Employee] = []
        self.is_saved: bool = True
        self.launch()
        # self.start()

    def start(self): # user interface
        help = """1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
"""
        print("Welcome to the Employee Records Manager!")
        print(help)
        while True:
            choice = input("Enter your choice: ")
            if choice.lower().strip() == "help":
                print(help)
                continue
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid input. Input must be an integer 1-6, or 'help'. Try again.")
                continue
            match choice:
                case 1:
                    e = self._employee_input()
                    self.update(e.employee_id, e)
                case 2:
                    print(self.view())
                case 3:
                    print(self.search(self._id_input(label="to search")))
                case 4:
                    old_id = self._id_input(label="to update")
                    e = self._employee_input(updated_id=old_id)
                    old = self.update(old_id, e)
                    print(f"{old} is updated to {e}")
                case 5:
                    e = self.delete(self._id_input("to remove"))
                    print(f"Deleted: {e}")
                case 6:
                    if not self.is_saved:
                        save = input("Data is not saved to the file. Do you wish to save and exit (Y), exit without saving (n), cancel all the changes and exit (q), or cancel exitting (c)? (Y/n/q/c) ").lower().strip()
                        if save == "y":
                            self.sync()
                            break
                        elif save == "n":
                            break
                        elif save == "q":
                            self.launch()
                            break
                        else:
                            continue
                case _:
                    print("Please enter number between 1 and 6, or type 'help' for instructions.")
    
    def view(self):
        """Returns print-ready string of all the employees in the list."""
        return "\n".join(i.row() for i in self.data)
    
    def search(self, employee_id: int):
        """Finds and returns employee details. 
        Returns None if not found"""
        e = None
        for i in self.data:
            if i.employee_id == employee_id:
                e = i
                break
        if e is not None:
            return e.row()
        else:
            return None
    
    def update(self, employee_id: int, employee: Employee):
        """Updates the employee with given id in the list. 
        Returns the employee before updating.
        Adds the employee to the list if not found, returning None."""
        self.is_saved = False
        index = None
        for i, e in enumerate(self.data):
            if e.employee_id == employee_id:
                index = i
                break
        if index is None:
            self.data.append(employee)
            return None
        else:
            old = self.data[index]
            self.data[index] = employee
            return old

    def delete(self, employee_id: int):
        """Removes the employee with given id from the list.
        Returns the removed employee, or None if the employee is not found."""
        for i, e in enumerate(self.data):
            if e.employee_id == employee_id:
                self.is_saved = False
                return self.data.pop(i)
        return None
    
    def clear(self):
        """Clears out the data."""
        self.data = []

    def is_unique(self, employee_id: int):
        """Returns True if the id is not reserved, and False if not."""
        return all(i.employee_id != employee_id for i in self.data)
    
    def generateID(self):
        return max(i.employee_id for i in self.data) + 1

    def sort(self, key: Callable = lambda x: x.employee_id, reverse: bool = False):
        """Returns sorted version of the list."""
        return sorted(self.data, key=key, reverse=reverse)

    def launch(self):
        """Launches the data from the file. 
        Skips invalid lines, and if an id appears more than once, considers the next ones as updates."""
        if not os.path.exists(self.db):
            raise FileNotFoundError(f"Configuration file not found: '{self.db}'")
        lines = []
        with open(self.db, "r") as file:
            lines = file.readlines()
        self.clear()
        for line in lines:
            try:
                employee_id, name, position, salary = map(lambda x: x.strip(), line.split(","))
                employee_id = int(employee_id)
                salary = int(salary)
            except ValueError:
                continue
            employee = Employee(employee_id, name, position, salary)
            self.update(employee_id, employee)
        self.is_saved = True

    def sync(self):
        """Writes the data to the file. The file will be created if it is not found."""
        with open(self.db, "w") as file:
            if len(self.data) > 0:
                file.write(self.view())
            self.is_saved = True
    
    def _employee_input(self, updated_id=-1):
        """Inputs employee data properly, and returns an Emoloyee instance with the data."""
        employee_id = -1
        while True:
            e_id = input("Enter Employee ID (integer/'auto'): ")
            if e_id.lower().strip() == 'auto':
                employee_id = self.generateID()
                print(f"ID chosen is: {employee_id}")
                break
            try:
                employee_id = int(e_id.strip())
            except ValueError:
                print("You must enter an integer, or 'auto' to let computer choose its unique id.")
                continue
            else:
                if employee_id < 0:
                    print("ID must be non-negative!")
                    continue
            if employee_id != updated_id and not self.is_unique(employee_id):
                c = input("This id already exists. Do you want to remove it (Y) or choose another ID (n)? ")
                if c.upper().strip() == "Y":
                    self.delete(employee_id)
                    break
                else:
                    continue
            else:
                break
        name = ""
        while not name:
            name = input("Enter the name: ").strip()
            if not name:
                print("Name cannot be empty!")
        position = ""
        while not position:
            position = input("Enter the position: ").strip()
            if not position:
                print("Position cannot be empty!")
        salary = -1
        while True:
            s = input("Enter the salary: ").strip()
            try:
                salary = int(s)
            except ValueError:
                print("Salary must be an integer!")
                continue
            else:
                if salary < 0:
                    print("Salary must be non-negative!")
                    continue
            break
        return Employee(employee_id, name, position, salary)
    
    def _id_input(self, label=""):
        """Inputs ID properly, without requiring it to be unique, and returns it."""
        if label:
            label = f" {label}"
        while True:
            e_id = input(f"Enter the Employee ID{label}: ")
            try:
                e_id = int(e_id)
            except ValueError:
                print("ID must be an integer!")
                continue
            else:
                if e_id < 0:
                    print("ID cannot be negative!")
                    continue
            return e_id





# To-Do Application:

import csv

class Task:

    def __init__(self, task_id: int, title: str, description: str, due_date: str, status: str):
        self.task_id: int = task_id
        self.title: str = title
        self.description: str = description
        self.due_date: str = due_date
        self.status: str = status

    def __str__(self):
        return f"Task({self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status})"
    
    def __iter__(self):
        yield self.task_id
        yield self.title
        yield self.description
        yield self.due_date
        yield self.status

    def row(self):
        """Returns a row view of Task for printing."""
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class ToDoApplication:

    def __init__(self, db: str = "tasks.csv"):
        self.db: str = db
        self.data: list[Task] = []
        self.is_saved: bool = True
        if not os.path.exists(self.db):
            raise FileNotFoundError(f"Configuration file not found: '{self.db}'")
        self.loadCSV()
        # self.start()

    def start(self): # user interface
        help = """1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit"""
        print("Welcome to the To-Do Application!")
        print(help)
        while True:
            a = input("\nEnter your choice: ").strip()
            if a.lower() == 'help':
                print(help)
                continue
            try:
                a = int(a)
            except ValueError:
                print("Input must be an integer (1-8) or 'help'. Try again.")
                continue
            match a:
                case 1:
                    task = self._task_input()
                    self.update(task.task_id, task)
                    print("Task added successfully!")
                case 2:
                    print("Tasks:")
                    print(self.view())
                case 3:
                    task_id = self._id_input("to update")
                    task = self._task_input()
                    self.update(task_id, task)
                    print("Task updated successfully!")
                case 4:
                    task_id = self._id_input("to delete")
                    self.delete(task_id)
                    print("Task deleted successfully!")
                case 5:
                    status = self._status_input()
                    print(self.view(self.filter_by_status(status)))
                case 6:
                    self.saveCSV()
                    print("Tasks are saved successfully!")
                case 7:
                    self.loadCSV()
                    print("Tasks are loaded successfully!")
                case 8:
                    if self.is_saved:
                        break
                    else:
                        q = input("You have some tasks not saved. Do you want to save and exit (Y), exit without saving (n), or cancel exitting (c)? ").strip().lower()
                        if q == "y":
                            self.saveCSV()
                            break
                        elif q == "n":
                            break
                        else:
                            continue

    # Base methods
    def view(self, data: list[Task] = None):
        """Returns a print-ready view of the Tasks. 
        Works with sliced or filtered data too via argument 'data'."""
        if not data:
            data = self.data
        return "\n".join(i.row() for i in data)

    def find(self, task_id: int):
        """Returns the index of the Task with the given id in the data. 
        If such Task is not found, returns None."""
        index = None
        for i, e in enumerate(self.data):
            if e.task_id == task_id:
                index = i
                break
        return index
    
    def update(self, task_id: int, task: Task):
        """Updates the Task with given id. Returns the old Task.
        If the Task with the given id is not found, adds the Task to the list, and returns None."""
        self.is_saved = False
        index = self.find(task_id)
        if index is None:
            self.data.append(task)
            return None
        else:
            old = self.data[index]
            self.data[index] = task
            return old

    def delete(self, task_id: int):
        """Deletes the Task with the given id and returns that deleted Task.
        If the Task doesn't exist, returns None."""
        index = self.find(task_id)
        if index is None:
            return None
        else:
            self.is_saved = False
            return self.data.pop(index)
    
    def clear(self):
        """Clears the data."""
        self.is_saved = False
        self.data = []

    def filter_by_status(self, status: str):
        """Returns the list of Tasks filtered by status."""
        return [i for i in self.data if i.status == status]
    
    def is_unique(self, task_id: int):
        """Checks if the Task ID is unique."""
        return self.find(task_id) is None
    
    def generate_id(self):
        """Generates a unique Task ID."""
        if len(self.data) < 1:
            return 1
        return max(max(i.task_id for i in self.data) + 1, 1)

    # These 2 methods below are the only ones to be changed if the file format is changed (e.g. to JSON).
    # I separated the base, input handling, and load/save, so that we only need to change load/save functions when changing file format.
    def loadCSV(self):
        """Reads the data from the file and changes the list 'data' to it."""
        self.clear()
        with open(self.db, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                row = [i.strip() for i in row]
                if len(row) != 5:
                    continue
                try:
                    row[0] = int(row[0])
                except ValueError:
                    continue
                else:
                    task = Task(*row)
                    self.update(task.task_id, task)
        self.is_saved = True

    def saveCSV(self):
        """Writes the data to the file."""
        with open(self.db, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(map(str, i) for i in self.data)
        self.is_saved = True

    # Input with exception handling and validation
    def _task_input(self):
        """Inputs a new Task and returns Task object with that value."""
        while True:
            task_id = input("Enter Task ID: ").strip()
            if task_id.lower() == 'auto':
                task_id = self.generate_id()
                break
            try:
                task_id = int(task_id)
            except ValueError:
                print("Task ID must be an integer. Try again, or type 'auto' if you want it generated automatically.")
                continue
            if task_id < 0:
                print("Task ID cannot be negative. Try again, or type 'auto' if you want it generated automatically.")
                continue
            if self.is_unique(task_id):
                break
            else:
                print("Task id must be unique. Try again, or type 'auto' if you want it generated automatically.")
                continue
        title = ""
        while True:
            title = input("Enter Title: ").strip()
            if not title:
                print("Title cannot be blank.")
            else:
                break
        description = ""
        while True:
            description = input("Enter Description: ").strip()
            if not description:
                print("Description cannot be blank.")
            else:
                break
        m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while True:
            due_date = map(str.strip, input("Enter Due Date (YYYY-MM-DD): ").split('-'))
            lst = []
            for i in due_date:
                if not i:
                    continue
                try:
                    lst.append(int(i))
                except ValueError:
                    continue
            if len(lst) == 3 and all(i > 0 for i in lst) and lst[1] <= 12 and lst[2] <= m[lst[1]]:
                due_date = f"{lst[0]:0>4}-{lst[1]:0>2}-{lst[2]:0>2}"
                break
            else:
                print("Invalid input. Please try again.")
                continue
        status = ""
        while True:
            status = input("Enter Status (Pending/In Progress/Completed): ").strip().lower()
            if status == "pending":
                status = "Pending"
            elif len(status) >= 10 and status[:2] == "in" and status[-9:] == "progress":
                status = "In Progress"
            elif status == "completed":
                status = "Completed"
            else:
                print("Status must be one of Pending, In Progress, or Completed.")
                continue
            break
        task = Task(task_id, title, description, due_date, status)
        return task

    def _id_input(self, label:str = ""):
        """Inputs a Task ID and returns it."""
        if label:
            label = f" {label.strip()}"
        while True:
            task_id = input(f"Enter the Task ID{label}: ").strip()
            try:
                task_id = int(task_id)
            except ValueError:
                print("Task ID must be an integer.")
                continue
            if task_id < 0:
                print("Task ID must be non-negative.")
                continue
            if not self.is_unique(task_id):
                break
            else:
                c = input("Task with such Task ID does not exist. Do you want to continue with that (Y/n)? ").strip().lower()
                if c == "y":
                    break
                else:
                    continue
        return task_id
    
    def _status_input(self):
        """Inputs and returns a Task Status."""
        while True:
            status = input("""1. Pending
2. In Progress
3. Completed
Enter the Status (1-3): """).strip()
            try:
                status = int(status)
            except ValueError:
                print("You must enter an integer between 1 and 3.")
                continue
            else:
                if status == 1:
                    status = "Pending"
                elif status == 2:
                    status = "In Progress"
                elif status == 3:
                    status = "Completed"
                else:
                    print("You must enter an integer between 1 and 3.")
                    continue
                break
        return status





# Zero Check Decorator

def check(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Denominator can't be zero"
    return wrapper

@check
def div(a, b):
   return a / b


# Employee Records Manager

name = "employees.txt"
with open(name, "w") as file:
    file.write("Employee ID, Name, Position, Salary\n")

print("""Choose an option (1-6):
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
def find(e_id):
    e_id = str(e_id).strip()
    with open(name, "r") as file:
        header = file.readline() 
        lines = file.readlines()
        for i in range(len(lines)):
            if e_id == lines[i].split(",")[0].strip():
                return (i, lines[i])

while True:
    n = int(input("> "))
    match n:
        case 1:
            record = input()
            if record:
                with open(name, "a") as file:
                    file.write(record + "\n")
        case 2:
            with open(name, "r") as file:
                print(file.read(), end="")
        case 3:
            e_id = input()
            employee = find(e_id)
            if employee:
                print(employee[1], end="")
            else:
                print("Not found")
        case 4:
            lines = []
            with open(name, "r") as file:
                lines = file.readlines()
            e_id = input()
            n = find(e_id)
            if n:
                n = n[0] + 1
                line = input()
                if line:
                    lines[n] = line + "\n"
                    with open(name, "w") as file:
                        file.writelines(lines)
            else:
                print("Id not found")
        case 5:
            e_id = input()
            n = find(e_id)
            lines = []
            with open(name, "r") as file:
                lines = file.readlines()
            if n and lines:
                n = n[0] + 1
                line = lines.pop(n)
                with open(name, "w") as file:
                    file.writelines(lines)
                    print("Removed", line, end="")
        case 6:
            break
                

# Word Frequency Counter

import re

name = "sample.txt"
content = ""
while not content:
    try:
        with open(name, "r") as file:
            content = file.read()
    except OSError:
        print("Please, create the sample.txt by typing in a paragraph")

words = re.findall(r"[a-z0-9]+", content.lower())

cnt = {}
for word in words:
    if word in cnt:
        cnt[word] += 1
    else:
        cnt[word] = 1
top = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

try:
    n = int(input("How many most common words? "))
except ValueError:
    n = 5
n = min(n, len(top))

report = f"Total words: {len(words)}\nTop {n} most common words:\n"
freport = f"Word Count Report\nTotal words: {len(words)}\nTop {n} words:\n"
for i in range(n):
    word, count = top[i]
    t = "time" if count == 1 else "times"
    report += f"{word} - {count} {t}\n"
    freport += f"{word} - {count}\n"

print(report, end="")
with open("word_count_report.txt", "w") as file:
    file.write(freport)
# with open("word_count_report.txt", "r") as file:
#     print(file.read())




                

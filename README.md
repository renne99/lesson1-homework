# 🐍 Python Learning Journey — Ndosi Automation

> A complete record of my Python fundamentals journey, covering variables, data structures, functions, Git workflows, and API integration.

---

## 📚 Table of Contents

- [About This Repository](#about-this-repository)
- [Lesson 1 — Python Basics](#lesson-1--python-basics)
- [Lesson 3 — Lists, Dictionaries, Loops & Functions](#lesson-3--lists-dictionaries-loops--functions)
- [Final Task — API Data Collector](#final-task--api-data-collector)
- [Git Workflow Used](#git-workflow-used)
- [Technologies & Tools](#technologies--tools)
- [What I Learned](#what-i-learned)

---

## About This Repository

This repository documents my progress through a structured Python automation course. Each lesson builds on the previous one, introducing new concepts and applying them through hands-on homework tasks. The final task ties everything together by consuming a live REST API, saving data locally, and searching through it — all using core Python skills.

---

## Lesson 1 — Python Basics

### 📌 What I Learned
- Variables and data types (`str`, `int`, `float`)
- Taking user input with `input()`
- Type conversion with `int()` and `float()`
- Printing formatted output using **f-strings**

### 📝 Task Description
Capture the **name**, **age**, and **height** of two users via the terminal, then display each user's information in a sentence and calculate their combined height.

### 💡 Key Concepts

```python
# Variables and input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

# F-string formatting
print(f"{name} is {age} years old and is {height} cm tall.")
```

### 📂 File
`Homework.py` — original version on the `main` branch.

---

## Lesson 3 — Lists, Dictionaries, Loops & Functions

### 📌 What I Learned
- **Lists** — storing multiple items in order
- **Dictionaries** — storing data as key-value pairs
- **For loops** — repeating code without duplication
- **Functions** — reusable, named blocks of code
- **Git branching** — creating feature branches and Pull Requests

### 📝 Task Description
Refactor the Lesson 1 homework to use:
- A **list of dictionaries** to store both users' data
- A **loop** to display each user's information
- A **function** to calculate total combined height

### 💡 Key Concepts

```python
# List of dictionaries
users = [
    {"name": "Alice", "age": 22, "height": 165.0},
    {"name": "Bob",   "age": 25, "height": 180.5}
]

# Loop through the list
for user in users:
    print(f"{user['name']} is {user['age']} years old and is {user['height']} cm tall.")

# Function
def calculate_total_height(users):
    total = users[0]["height"] + users[1]["height"]
    return total

print(f"Total combined height: {calculate_total_height(users)} cm.")
```

### 📂 File
`Homework.py` — updated version on the `lesson3-homework` branch.

### 🔀 Git Branch
`lesson3-homework` → Pull Request into `main`

---

## Final Task — API Data Collector

### 📌 What I Learned
- Sending HTTP GET requests using the `requests` library
- Parsing and working with **JSON data**
- Writing data to a file using `json.dump()`
- Reading data from a file using `json.load()`
- Searching through a list of dictionaries
- Handling **found** and **not found** scenarios with clear user messages

### 📝 Task Description

**Task 1 — Get API Data:**
Send a GET request to the live API endpoint and return the data.

**Task 2 — Save Data to File:**
Take the API response and save it to a local `groups.json` file.

**Task 3 — Read and Search Data:**
Read the saved file, ask the user for a group name, and search for it. Display a success message with the Group ID if found, or an error message if not.

### 🌐 API Endpoint
```
GET https://www.ndosiautomation.co.za/APIDEV/groups
```

### 💡 Key Concepts

```python
import requests
import json

# Task 1 — GET request
def get_api_data():
    url = "https://www.ndosiautomation.co.za/APIDEV/groups"
    response = requests.get(url)
    return response.json()

# Task 2 — Save to file
def save_data_to_file(data, filename="groups.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Task 3 — Search
def search_group():
    with open("groups.json", "r") as file:
        data = json.load(file)

    search_name = input("Enter the group name to search for: ")

    for group in data["data"]:
        if group["Name"].lower() == search_name.lower():
            print(f"✅ Group found! Name: '{group['Name']}' | ID: {group['Id']}")
            return

    print(f"❌ Error: Group '{search_name}' was not found.")
```

### 📦 Dependency
```bash
pip install requests
```

### 📂 File
`api_collector.py`

---

## Git Workflow Used

Throughout this course I followed a professional Git workflow:

```
main branch
  └── lesson3-homework branch   ← feature branch
        └── Pull Request → main ← code review & merge
```

### Commands Used

```bash
# Create and switch to a new branch
git checkout -b lesson3-homework

# Stage changes
git add Homework.py

# Commit with a meaningful message
git commit -m "Update homework using lists, dictionaries, loops and functions"

# Push branch to GitHub
git push origin lesson3-homework
```

Then on GitHub: **New Pull Request** → `lesson3-homework` into `main` → Submit for review.

---

## Technologies & Tools

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| PyCharm | IDE used for writing and running code |
| Git & GitHub | Version control and repository hosting |
| `requests` library | Sending HTTP GET requests |
| `json` module | Reading and writing JSON data |
| REST API | Live data source for the final task |

---

## What I Learned

By the end of this course I was able to:

- Write clean Python code using variables, input, and f-strings
- Organise data using lists and dictionaries
- Use loops to avoid repetitive code
- Write reusable functions
- Work with Git branches and Pull Requests like a professional developer
- Connect to a live REST API, save the data locally, and search through it
- Handle user input and display meaningful success and error messages

---

> 💬 *"Every expert was once a beginner. This repository is proof of that journey."*

import json
import os

FILE = "todo.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {mark} {t['title']}")

tasks = load()

while True:
    print("\n1) Show  2) Add  3) Done  4) Delete  5) Exit")
    choice = input("> ")

    if choice == "1":
        show(tasks)
    elif choice == "2":
        title = input("Task: ")
        tasks.append({"title": title, "done": False})
        save(tasks)
        print("Added.")
    elif choice == "3":
        show(tasks)
        try:
            n = int(input("Task number: "))
            tasks[n - 1]["done"] = True
            save(tasks)
        except (ValueError, IndexError):
            print("Invalid number.")
    elif choice == "4":
        show(tasks)
        try:
            n = int(input("Task number: "))
            tasks.pop(n - 1)
            save(tasks)
        except (ValueError, IndexError):
            print("Invalid number.")
    elif choice == "5":
        break

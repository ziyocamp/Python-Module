def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added!")


def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
        return
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i + 1}. {status} {t['task']}")


def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("🎉 Task marked as done!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Deleted task: {removed['task']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")


def main():
    tasks = []
    while True:
        print("\n📋 TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye! All tasks lost (not saved).")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()

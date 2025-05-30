from utils import (
    show_menu,
    add_task,
    view_tasks,
    mark_done,
    delete_task
)


def main():
    tasks = []
    while True:
        show_menu()

        choice = input("Choose an option (1-5): ") # "1"

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


main()

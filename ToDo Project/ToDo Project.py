def menu():
    print("\n==== To-Do List ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    tasks = []

    while True:
        menu()
        choice = input("What do you want to do (1-4): ")

        if choice == "1":
            if not tasks:
                print("To-Do list is empty.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added.")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                try:
                    index = int(input("Enter the task number to remove: "))
                    if 1 <= index <= len(tasks):
                        removed = tasks.pop(index - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import ToDoFunctions

def main():
    filename = "Task_Records.txt"
    ToDoFunctions.loadfile(filename)

    """Welcome Messages"""
    print("Welcome to the To-Do App.\n What would you like to do today? \n Choose from the following options: \n")

    while True:
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark tasks as complete")
        print("4. Remove tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if (choice == "1"):
            print("Add a task: ")
            name = input("Enter the task name: ").strip().lower()
            description = input("Describe the task: ").strip().lower()
            deadline = input("Enter the deadline for the task in hours").strip().lower()
            status = "incomplete"

            task = ToDoFunctions.addTasks(name, description, deadline, status)

            content = f"Task {task['name']} has been added"
            ToDoFunctions.appendRecords(filename, content)

            print(content)
        elif choice == "2":
            tasks = ToDoFunctions.viewTasks()

            if tasks:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. Name: {task['name']} \n  Description: {task['description']} \n Deadline: {task['deadline']} hours \n Status: {task['status']}")
            else:
                print("No tasks to show.")
        elif (choice == "3"):
            name = input("Enter the task name: ").strip().lower()

            task = ToDoFunctions.markTasks(name)

            if task:
                if task["status"] == "incomplete":
                    task["status"] = "complete"
                    content = f"Congratulations! Task '{task['name']}' has been completed."
                    ToDoFunctions.appendRecords(filename, content)

                    print(content)
                elif task["status"] == "complete":
                    print("Task already completed")
                else:
                    print("Task doesn't exist.")
        elif (choice == "4"):
            tasks = ToDoFunctions.viewTasks()

            if tasks:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. Name: {task['name']} \n  Description: {task['description']} \n Deadline: {task['deadline']} hours \n Status: {task['status']}")
                index = int(input("Enter a task number: ").strip())
                removedTask = ToDoFunctions.removeTasks(index)
                print(f"Task {removedTask['name']} has been removed.")
            else:
                print("No tasks to show.")
        elif (choice == "5"):
            print("Thanks for using the To-Do App \n See you next time!")
            break
        else:
            print("Invalid input")
            
            












if (__name__ == "__main__"):
    main()
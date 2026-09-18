from models import Task, Project
from storage import save_data, load_data

projects = load_data()

while True:
    print("\n-- Task Manager --")
    print("1. Create project")
    print("2. View projects")
    print("3. Add task")
    print("4. Search task")
    print("5. Edit task")
    print("6. Change task status")
    print("7. Change task priority")
    print("8. Delete task")
    print("10. Save & Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Project name: ")
        project = Project(name)
        projects.append(project)
        print("Project created")

    elif choice == "2":
        for project in projects:
            print(project.name)

        for task in project.tasks:
            print(
                f"Title: {task.title}, "
                f"Description: {task.description}, "
                f"Due Date: {task.due_date}, "
                f"Priority: {task.priority}, "
                f"Status: {task.status}"
            )

    elif choice == "3":
        project_name = input("Project name: ")

        selected_project = None

        for project in projects:
            if project.name == project_name:
                selected_project = project
                break

        if selected_project is None:
            print("Project not found.")
        else:
            title = input("Task title: ")
            description = input("Task description: ")
            due_date = input("Due date: ")
            priority = input("Priority (low/medium/high): ")

            try:
                task = Task(title, description, due_date, priority)
                selected_project.add_task(task)

                print("Task added")
            except ValueError as error:
                print(error)

    elif choice == "4":
        title = input("Task title: ")

        found_task = None

        for project in projects:
            task = project.find_task(title)

            if task is not None:
                found_task = task
                break

        if found_task is None:
            print("Task not found.")
        else:
            print(f"Title: {found_task.title}")
            print(f"Description: {found_task.description}")
            print(f"Due date: {found_task.due_date}")
            print(f"Priority: {found_task.priority}")
            print(f"Status: {found_task.status}")

    elif choice == "5":
        title = input("Task title: ")

        found_task = None

        for project in projects:
            task = project.find_task(title)

            if task is not None:
                found_task = task
                break

        if found_task is None:
            print("Tass is not found")
        else:
            new_title = input("New title: ")
            new_description = input("New description: ")
            new_due_date = input("New due date: ")

            if new_title == "":
                new_title = None

            if new_description == "":
                new_description = None

            if new_due_date == "":
                new_due_date = None

            found_task.edit(new_title, new_description, new_due_date)

            print("Task edited")

    elif choice == "6":
        title = input("Task title: ")

        found_task = None

        for project in projects:
            task = project.find_task(title)

            if task is not None:
                found_task = task
                break

        if found_task is None:
            print("Tass is not found")

        else:
            new_status = input("New status  (pending/in-progress/completed): ")

            try:
                found_task.change_status(new_status)
                print("Task status changed")
            except ValueError as error:
                print(error)

    elif choice == "7":
        title = input("Task title: ")

        found_task = None

        for project in projects:
            task = project.find_task(title)

            if task is not None:
                found_task = task
                break

        if found_task is None:
            print("Tass is not found")
        else:
            new_priority = input("New priority   (low/medium/high): ")

            try:
                found_task.change_priority(new_priority)
                print("Task priority is changed")
            except ValueError as error:
                print(error)

    elif choice == "8":
        title = input("Task title: ")

        found_task = None
        found_project = None

        for project in projects:
            task = project.find_task(title)

            if found_task is not None:
                found_project = project
                found_task = task
                break

        if found_task is None:
            print("Tass is not found")
        else:
            found_project.delete_task(found_task)
            print("Task deleted")

    elif choice == "10":
        save_data(projects)
        print("Saved")
        break
import json
from models import Task, Project

def save_data(projects):
    data = []

    for project in projects:
        data.append(project.project_serialization())

    with open("tasks.json", "w") as file:
        json.dump(data, file)

def load_data():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    projects = []

    for project_data in data:
        project = Project(project_data["name"])

        for task_data in project_data["tasks"]:
            task  = Task (
                task_data["title"],
                task_data["description"],
                task_data["due_date"],
                task_data["priority"]
            )

            task.change_status(task_data["status"])
            project.add_task(task)

        projects.append(project)

    return projects


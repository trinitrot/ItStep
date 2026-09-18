from decorators import check_value

class BaseTask:
    def __init__ (self, title, description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date


class Task(BaseTask):
    ALLOWED_STATUSES = ("pending", "in-progress", "completed")
    ALLOWED_PRIORITIES = ("low", "medium", "high")

    def __init__ (self, title, description, due_date, priority):
        super().__init__(title, description,due_date)

        self.change_priority(priority)
        self.__status = "pending"

    @property
    def status(self):
        return self.__status

    @property
    def priority(self):
        return self.__priority

    @check_value(ALLOWED_STATUSES)
    def change_status(self, new_status):
        self.__status = new_status

    @check_value(ALLOWED_PRIORITIES)
    def change_priority(self, new_priority):
        self.__priority = new_priority

    def edit(self, title=None, description=None, due_date=None):
        if title is not None:
            self.title = title

        if description is not None:
            self.description = description

        if due_date is not None:
            self.due_date = due_date

    def task_serialization(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task

        return None

    def project_serialization(self):
        tasks_data = []

        for task in self.tasks:
            tasks_data.append(task.task_serialization())

        return {
            "name": self.name,
            "tasks": tasks_data
        }














    # def task_deserialization(self, data):
    #     task = Task(
    #         data["title"],
    #         data["description"],
    #         data["due_date"],
    #         data["priority"]
    #     )
    #
    #     return task




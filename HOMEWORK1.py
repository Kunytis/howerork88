#Этот проект быс скопирован из другого так как другой проект не получалось выставить на гитхаб!!!

class Task:
    def __init__ (self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def task_completed(self):
        self.completed = True

    def __str__(self):
        status = "done" if self.completed else "error"
        return f"name: {self.name}, about {self.description}, deadline??? {self.deadline}, status ..{status}."

class Manager:
    def __init__(self):
        self.task = []

    def add_task(self, title, description, deadline):
       task = Task(title, description, deadline)
       self.task.append(task)
       print(f"task {title} added")

    def remove_tasl(self, title):
        for task in self.tasks:
            if task.title == title:
                task.task_remove(task)
                print(f" smth {title} deleted lol")

            return
        print(f"smth {title} not found, try anothr title")

    def task_completed(self, title):
        for task in self.taks:
            if task.title == title:
               task.task_complete()
            print(f"Task {title} added like completed")
            return
        print(f"Task {title} not found")

    def show_tasks(self):
        if not self.tasks:
            print("empty!")
            return
        print("list!")
        for task in self.tasks:
            print(task)
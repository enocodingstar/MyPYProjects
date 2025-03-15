"""Storing records in a file"""
def loadfile(filename):
    try:
        with open(filename, "w") as file:
            file.write("All activities are recorded and stored here.\n")
    except FileExistsError:
        print(f"File {filename} already exists")
    return[]

"""Appending a record to the file"""
def appendRecords(filename, content):
    try:
        with open(filename, "a") as file:
            file.write(content + "\n")
    except Exception as e:
        print("An error occured")
    return filename, content


global tasks
tasks = []


"""Add tasks"""
def addTasks(name, description, deadline, status):
    task = {"name": name, "description": description, "deadline": deadline, "status": status}
    tasks.append(task)
    return task


"""View tasks"""
def viewTasks():
    return tasks


"""Mark task as complete"""
def markTasks(name):
    for task in tasks:
        if task["name"] == name:
            return task
        else:
            return None

"""Removing tasks"""
def removeTasks(index):
        removedTask = tasks.pop(index - 1)
        return removedTask



            
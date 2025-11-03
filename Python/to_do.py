import os
import json

class TodoList:
    def __init__(self, filename='todo_list.json'):
        self.filename= filename
        self.tasks = []
        self.load_tasks()

    def add_tasks(self, title):
        if not title or not isinstance(title, str):
            raise ValueError("Task title must be a non-empty string.")
        task = {'Title':title, "Completed":False}
        self.tasks.append(task)
        self.save_tasks()
    
    def remove_task(self, title):
        found = False
        for task in self.tasks:
            if task['Title'] == title:
                self.tasks.remove(task)
                found = True
                break
        if not found:
            raise ValueError("Task not found")
        
        self.save_tasks()

    def mark_complete(self, title):
        for task in self.tasks:
            if task['Title'] == title:
                task['Completed']= True
                self.save_tasks()
                return
        raise ValueError("Task not found")
    
    def list_tasks(self):
        return self.tasks
    
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    self.tasks= json.load(f)
                except json.JSONDecodeError:
                    self.tasks=[]
        else:
            self.tasks=[]
    
    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()

if __name__ == "__main__":
    todo = TodoList()

    while True:
        print("\n To-Do List Menu: ")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as complete")
        print("4. List tasks")
        print("5. Clear all tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ").strip()
            todo.add_tasks(title)
            print("Task added.")
        elif choice == '2':
            title = input("Enter task title to remove: ").strip()
            try:
                todo.remove_task(title)
                print("Task removed.")
            except ValueError as e:
                print(e)
        elif choice == '3':
            title = input("Enter task title to mark as complete: ").strip()
            todo.mark_complete(title)
            print("Task is now completed.")
        elif choice == '4':
            tasks = todo.list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks: ")
                for g, task in enumerate(tasks, 1):
                    status = "Completed" if task['Completed'] else "Pending"
                    print(f"{g}. {task['Title']} - {status}")
        elif choice == '5':
            todo.clear_tasks()
            print("All tasks cleared.")
        
        elif choice == '6':
            print ("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")
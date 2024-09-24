import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = {}
        self.task_id = 1
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks[self.task_id] = {'task': task, 'completed': False}
            self.task_listbox.insert(tk.END, f"{self.task_id}: {task} [❌]")
            self.task_id += 1

    def update_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_id = task_index + 1
            new_task = simpledialog.askstring("Update Task", "Enter the new task description:")
            if new_task:
                self.tasks[task_id]['task'] = new_task
                self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def complete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_id = task_index + 1
            self.tasks[task_id]['completed'] = True
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task_id, task_info in self.tasks.items():
            status = "DONE" if task_info['completed'] else "Incomplete"
            self.task_listbox.insert(tk.END, f"{task_id}: {task_info['task']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
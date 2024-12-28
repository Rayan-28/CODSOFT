import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        
        # Create main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Create listbox
        self.task_listbox = tk.Listbox(
            self.frame,
            width=40,
            height=15,
            selectmode=tk.SINGLE,
            selectbackground="#a6a6a6"
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Connect listbox to scrollbar
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Create entry box
        self.task_entry = tk.Entry(
            self.root,
            width=40
        )
        self.task_entry.pack(pady=10)

        # Create button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Add task button
        self.add_button = tk.Button(
            self.button_frame,
            text="Add Task",
            command=self.add_task
        )
        self.add_button.grid(row=0, column=0, padx=5)

        # Delete task button
        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete Task",
            command=self.delete_task
        )
        self.delete_button.grid(row=0, column=1, padx=5)

        # Mark complete button
        self.complete_button = tk.Button(
            self.button_frame,
            text="Mark Complete",
            command=self.mark_complete
        )
        self.complete_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_complete(self):
        try:
            selected_task = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task)
            if not task.startswith("✓ "):
                self.task_listbox.delete(selected_task)
                self.task_listbox.insert(selected_task, "✓ " + task)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = TodoList(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.selected_task = None

        self.root.geometry("300x350")
        self.root.title("To-Do List")
        
        self.label = tk.Label(root, text="Tasks", fg="white", bg="grey", height=1, width=30, font=("Arial", 15, "bold"))
        self.label.pack(fill=tk.X)

        self.tasks_frame = tk.Frame(root, bg="#1e1e1e")
        self.tasks_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.entry = tk.Entry(root, bg='#404040', insertbackground='white',fg="white", relief=tk.FLAT)
        self.entry.place(relx=0.5, rely=0.93, anchor="center", width=280)
        self.entry.bind('<Return>', lambda e: self.add_task())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            task_frame = tk.Frame(self.tasks_frame, bg="#2d2d2d")
            task_frame.pack(fill=tk.X, pady=2)

            task_label = tk.Label(task_frame, text=task, bg="#2d2d2d", fg="white",pady=5, padx=5)
            task_label.pack(side=tk.LEFT)

            delete_btn = tk.Button(task_frame, text="✕", bg="#2d2d2d", fg="red",border=0, command=lambda: self.delete_task(task_frame))
            delete_btn.pack(side=tk.RIGHT)

            task_frame.bind('<Button-1>', lambda e: self.select_task(task_frame))
            task_label.bind('<Button-1>', lambda e: self.select_task(task_frame))

            self.tasks.append(task_frame)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def select_task(self, task_frame):
        if self.selected_task:
            self.selected_task.configure(bg="#2d2d2d")
            for widget in self.selected_task.winfo_children():
                widget.configure(bg="#2d2d2d")

        
        task_frame.configure(bg="#404040")
        for widget in task_frame.winfo_children():
            widget.configure(bg="#404040")
        self.selected_task = task_frame

    def delete_task(self, task_frame):
        if task_frame in self.tasks:
            self.tasks.remove(task_frame)
            task_frame.destroy()

def main():
    root = tk.Tk()
    root.configure(bg="#1e1e1e")
    todo = TodoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x400")

# Task list
tasks = []

# Functions
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        tasks.remove(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Entry field and buttons
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

del_btn = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
del_btn.pack(pady=5)

# Task list display
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Run the app
root.mainloop()

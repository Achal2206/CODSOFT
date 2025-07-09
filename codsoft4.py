import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected)
    except IndexError:
        messagebox.showinfo("Selection Error", "Please select a task to delete.")

def mark_completed():
    try:
        selected = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected)
        tasks_listbox.delete(selected)
        tasks_listbox.insert(tk.END, f"✔️ {task}")
    except IndexError:
        messagebox.showinfo("Selection Error", "Please select a task to mark as completed.")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x400")

# Entry field
tk.Label(root, text="Enter a Task:").pack(pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Task list
tasks_listbox = tk.Listbox(root, width=45, height=10)
tasks_listbox.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", width=12, command=add_task).pack(pady=2)
tk.Button(root, text="Delete Task", width=12, command=delete_task).pack(pady=2)
tk.Button(root, text="Mark Completed", width=12, command=mark_completed).pack(pady=2)

# Start GUI
root.mainloop() 
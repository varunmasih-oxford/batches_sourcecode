# 1. What is Tkinter
   Tkinter is Python’s built-in library for creating 
   GUI (Graphical user interface) applications like windows, buttons, labels, text boxes, forms, etc.
   It requires no installation because it comes with Python.


# 2. Creating Your First Tkinter Window

--python
import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x300")

root.mainloop()
--

Explanation:
Tk() creates the window
title() sets the title
geometry() sets the size
mainloop() keeps the window open

# 3. Basic Widgets: Label, Entry, Button

--python
import tkinter as tk

root = tk.Tk()
root.title("Widgets Demo")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

def show_name():
    user_name = entry.get()
    result_label.config(text=f"Hello {user_name}!")

button = tk.Button(root, text="Submit", command=show_name)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
--

# 4. Layout Options
   pack(): simple stacking
   grid(): table-like positioning
   place(): absolute positioning

Example:

--python
label = tk.Label(root, text="Name:")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)
--

# 5. Message Box

--python
from tkinter import messagebox
messagebox.showinfo("Title", "This is a message")
--

# 6. Adding Colors and Fonts

--python
tk.Label(root, text="Hello", bg="yellow", fg="blue", font=("Arial", 16)).pack()
--

---

Small Project: To-Do List App (Beginner Project)

Features:
Add tasks
Delete selected task
Save tasks to file
Load tasks when program starts

Complete Code:

--python
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task, width=20).pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_task, width=20).pack()

tk.Button(root, text="Save Tasks", command=save_tasks, width=20).pack()

load_tasks()

root.mainloop()
--


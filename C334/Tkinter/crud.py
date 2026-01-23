import tkinter as tk
from tkinter import messagebox

# ------- Global List to Store Records -------
records = []  # each item = {"name":..., "age":...}

# ------- Functions -------
def add_record():
    name = name_entry.get()
    age = age_entry.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    records.append({"name": name, "age": age})
    refresh_listbox()
    clear_fields()

def refresh_listbox():
    listbox.delete(0, tk.END)
    for i, r in enumerate(records):
        listbox.insert(tk.END, f"{i+1}. {r['name']} - {r['age']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def select_record(event):
    try:
        index = listbox.curselection()[0]
        selected = records[index]
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        name_entry.insert(0, selected["name"])
        age_entry.insert(0, selected["age"])
    except:
        pass

def update_record():
    try:
        index = listbox.curselection()[0]
    except:
        messagebox.showerror("Error", "Select a record to update!")
        return

    name = name_entry.get()
    age = age_entry.get()

    records[index] = {"name": name, "age": age}
    refresh_listbox()
    clear_fields()

def delete_record():
    try:
        index = listbox.curselection()[0]
    except:
        messagebox.showerror("Error", "Select a record to delete!")
        return

    del records[index]
    refresh_listbox()
    clear_fields()

# ------- Tkinter GUI -------
root = tk.Tk()
root.title("Simple CRUD App")
root.geometry("400x400")

# Labels & Entries
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Buttons
tk.Button(root, text="Add", command=add_record).pack(pady=5)
tk.Button(root, text="Update", command=update_record).pack(pady=5)
tk.Button(root, text="Delete", command=delete_record).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_record)

root.mainloop()

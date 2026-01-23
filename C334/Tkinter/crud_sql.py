import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------- DATABASE FUNCTIONS -----------------------
def connect_db():
    conn = sqlite3.connect("people.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS people(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_record(name, age):
    conn = sqlite3.connect("people.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO people(name, age) VALUES (?,?)", (name, age))
    conn.commit()
    conn.close()

def fetch_records():
    conn = sqlite3.connect("people.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM people")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_record(id, name, age):
    conn = sqlite3.connect("people.db")
    cur = conn.cursor()
    cur.execute("UPDATE people SET name=?, age=? WHERE id=?", (name, age, id))
    conn.commit()
    conn.close()

def delete_record(id):
    conn = sqlite3.connect("people.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM people WHERE id=?", (id,))
    conn.commit()
    conn.close()

# ----------------------- GUI FUNCTIONS -----------------------
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for row in fetch_records():
        tree.insert("", tk.END, values=row)

def add_data():
    name = name_entry.get()
    age = age_entry.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "All fields required!")
        return

    insert_record(name, age)
    refresh_table()
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def on_row_select(event):
    try:
        item = tree.selection()[0]
        data = tree.item(item)["values"]
        global selected_id
        selected_id = data[0]

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

        name_entry.insert(0, data[1])
        age_entry.insert(0, data[2])
    except:
        pass

def update_data():
    try:
        update_record(selected_id, name_entry.get(), age_entry.get())
        refresh_table()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select a record first")

def delete_data():
    try:
        delete_record(selected_id)
        refresh_table()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select a record first")


# ----------------------- TKINTER UI -----------------------
connect_db()

root = tk.Tk()
root.title("Tkinter CRUD with SQLite")
root.geometry("500x450")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Button(root, text="Add", width=20, command=add_data).pack(pady=5)
tk.Button(root, text="Update", width=20, command=update_data).pack(pady=5)
tk.Button(root, text="Delete", width=20, command=delete_data).pack(pady=5)

# Treeview Table
columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10, fill='both')

tree.bind("<<TreeviewSelect>>", on_row_select)

refresh_table()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Creating Tkinter Window

# root = tk.Tk()
# root.title('hey this is my first app')
# root.geometry("400x300")
# root.mainloop()


# Basic Widgets: Label, Entry, Button

# root = tk.Tk()  
# root.title("Widgets Demo")

# label = tk.Label(root,text="this is first line of window")
# label.pack()

# entry = tk.Entry(root)
# entry.pack()

# button = tk.Button(root, text="Submit")
# button.pack()

# root.geometry("400x300")
# root.mainloop()



root = tk.Tk()
# root.title("Show Name")

# label = tk.Label(root,text="Enter Your Name: ")
# label.pack()

# entry = tk.Entry(root)
# entry.pack()

# def show_name():
#     name_detail = entry.get()
#     result_label.config(text=f"Hello {name_detail}")

# button = tk.Button(root, text="Submit", command=show_name)
# button.pack()

# result_label = tk.Label(root, text="")
# result_label.pack()


# root.geometry("400x300")
# root.mainloop()





tk.Label(root, text="Hello", bg="yellow", fg="blue", font=("Arial", 16)).pack()

messagebox.showinfo("Title", "This is a message")


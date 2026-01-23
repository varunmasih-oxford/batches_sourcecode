import tkinter as tk

root_grid = tk.Tk()
root_grid.title("Grid Example (Login Form)")
root_grid.geometry("300x450")

# Configure padding for all widgets in the grid
# padx and pady add horizontal and vertical space around the widgets
# sticky="w" aligns widgets to the West (left) within their cell
padding_options = {'padx': 10, 'pady': 5, 'sticky': tk.W}

# --- Widgets ---

# Row 0: Username Label and Entry
tk.Label(root_grid, text="Username:").grid(row=0, column=0, **padding_options)
username_entry = tk.Entry(root_grid, width=20)
username_entry.grid(row=0, column=1, **padding_options)

# Row 1: Password Label and Entry
tk.Label(root_grid, text="Password:").grid(row=1, column=0, **padding_options)
password_entry = tk.Entry(root_grid, show="*", width=20) # show="*" hides password characters
password_entry.grid(row=1, column=1, **padding_options)

# Row 2: Login Button (spanning two columns)
# sticky="we" makes the button expand horizontally across both columns
tk.Button(root_grid, text="Login").grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

# --- Make columns stretchable (optional but recommended for responsive design) ---
# This tells the grid that column 1 should grow if the window is resized
root_grid.columnconfigure(1, weight=1)

root_grid.mainloop()

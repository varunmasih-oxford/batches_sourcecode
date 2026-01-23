import tkinter as tk

root_place = tk.Tk()
root_place.title("Place Example (Absolute Positioning)")
# Set a fixed size for the window as 'place' doesn't handle resizing well automatically
root_place.geometry("400x200") 
root_place.resizable(False, False) # Prevent window resizing

# --- Widgets ---

# Button 1: Placed at absolute coordinates (50 pixels from left, 30 pixels from top)
button1 = tk.Button(root_place, text="Button 1 (x=50, y=10)", bg="lightblue")
button1.place(x=50, y=10)

# Label 1: Placed using relative positioning (relx=0.5, rely=0.5)
# This places the top-left corner near the center of the parent window
label1 = tk.Label(root_place, text="Label 1 (relative center)", bg="lightgreen")
label1.place(relx=0.5, rely=0.5)

# Button 2: Placed using relative width and height (fills half the width, quarter the height)
# Anchor 'center' positions the widget's center at the specified (relx, rely) coordinates
button2 = tk.Button(root_place, text="Button 2 (Relative Size & Anchor)", bg="salmon")

button2.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.25, anchor=tk.CENTER)

# A simple label at a fixed spot near the bottom right
tk.Label(root_place, text="Fixed Bottom Right", bg="yellow").place(x=300, y=170)

root_place.mainloop()

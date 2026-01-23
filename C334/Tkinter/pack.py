import tkinter as tk

root_pack = tk.Tk()
root_pack.title("Pack Example")
root_pack.geometry("200x150")

tk.Label(root_pack, text="Top (Red)", bg="red", fg="white", height=2).pack(fill=tk.BOTH, expand=True)

tk.Label(root_pack, text="Middle (Green)", bg="green", fg="white", height=2).pack(fill=tk.BOTH, expand=True)

tk.Label(root_pack, text="Bottom (Blue)", bg="blue", fg="white", height=2).pack(fill=tk.BOTH, expand=True)

root_pack.mainloop()

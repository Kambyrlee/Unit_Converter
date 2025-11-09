from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
        pass

# Set up window with title.
root = Tk()
root.title("Unit Converter")

# Create and place main frame.
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Create and place feet entry box.
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # Width in characters.
feet_entry.grid(column=2, row=1, sticky=(W,E))

# Create and place meters result box.
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Create and place "Calculate" button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# Create and place static text.
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=E)

# Dynamic grid size when window resized.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Add extra padding for visual clarity.
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# UX helpers
feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()


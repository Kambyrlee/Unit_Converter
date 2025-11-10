from tkinter import *
from tkinter import ttk
from converters.feet_to_meters import FeetToMeters
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def start_conversion():
    choice = conversion.get()
    match choice:
        case "Feet to Meters":
            FeetToMeters(root)

root = Tk()
root.title("Unit Converter")

# Create and place main frame.
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Set up dropdown menu.
conversion = StringVar()
ttk.Label(mainframe, text="Select desired conversion:").grid(column=1, row=0)
conversion_box = ttk.Combobox(mainframe, 
             textvariable=conversion, 
             values=("Feet to Meters", "Meters to Feet"), 
             state="readonly")
conversion_box.grid(column=1, row=1, pady=5)
conversion_box.current(0)

ttk.Button(mainframe, text="Start", command=start_conversion).grid(column=1, row=2, pady=10)

# FeetToMeters(root)
root.mainloop()

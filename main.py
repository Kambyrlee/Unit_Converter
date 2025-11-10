from tkinter import *
from tkinter import ttk
from converters.feet_to_meters import FeetToMeters
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up window with title.
root = Tk()
FeetToMeters(root)
root.mainloop()

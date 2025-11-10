from tkinter import *
from tkinter import ttk

class CmToInches:
    def __init__(self, root):
        root.title("Centimeters to Inches")

        # Create and place main frame.
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Create and place centimeters entry box.
        self.cm = StringVar()
        cm_entry = ttk.Entry(mainframe, width=7, textvariable=self.cm)
        cm_entry.grid(column=2, row=1, sticky=(W,E))

        # Create and place inches result box.
        self.inches = StringVar()
        ttk.Label(mainframe, textvariable=self.inches).grid(column=2, row=2, sticky=(W, E))

        # Create and place "Calculate" button
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        # Create and place static text.
        ttk.Label(mainframe, text="centimeters").grid(column=3, row=1, sticky=E)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text="inches").grid(column=3, row=2, sticky=E)

        # Dynamic grid size when window resized.
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Add extra padding for visual clarity.
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        # UX helpers
        cm_entry.focus()
        root.bind("<Return>", self.calculate)
    
    def calculate(self, *args):
        try:
            value = float(self.cm.get())
            self.inches.set(round(0.393701 * value, 4))
        except ValueError:
            pass
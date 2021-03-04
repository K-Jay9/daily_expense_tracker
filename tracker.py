from tkinter import Tk
from tkinter.ttk import Frame, Button, Style


# Code Constants and variables

NAME = 'Daily Expense Tracker'
DAILY = 'Daily'
WEEKLY = 'Weekly'
MONTHLY = 'Monthly'
GEO = '720x640'


def initUI(root):

    # Adding the title to the window
    root.title(NAME)

    # Initilise the Geometry
    root.geometry(GEO)

    daily = Button(root, text=DAILY, style="C.TButton")
    daily.grid(row=0, column=1, sticky='nesw')

    weekly = Button(root, text=WEEKLY, style="C.TButton")
    weekly.grid(row=0, column=2, sticky='nesw')

    monthly = Button(root, text=MONTHLY, style="C.TButton")
    monthly.grid(row=0, column=3, sticky='nesw')

    

def styling(root):
    # tell tcl where to find the awthemes packages
    root.tk.eval("""
    set base_theme_dir awthemes/

    package ifneeded awthemes 10.2.1 \
        [list source [file join $base_theme_dir awthemes.tcl]]
    package ifneeded colorutils 4.8 \
        [list source [file join $base_theme_dir colorutils.tcl]]
    package ifneeded awdark 7.11 \
        [list source [file join $base_theme_dir awdark.tcl]]
    package ifneeded awlight 7.9 \
        [list source [file join $base_theme_dir awlight.tcl]]
    """)
    # load the awdark and awlight themes
    root.tk.call("package", "require", 'awdark')
    root.tk.call("package", "require", 'awlight')

    # Initialising Style and loading in a dark thene
    style = Style()
    style.theme_use('awdark')

    #configure buttons
    style.configure("TButton", padding=6, relief="flat")

    # button active tweaks
    style.map("C.TButton",
    foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', 'white'), ('active', 'white')]
    )

def main(root):
    # Add the Theme initilise the UI
    styling(window)
    initUI(window)


# Initialising the window
window = Tk()
main(window)
# Starting the mainloop
window.mainloop()
from tkinter import Tk, BOTTOM, LEFT, RIGHT, CENTER, TOP, BOTH
from tkinter.ttk import Frame, Button, Style


# Code Constants and variables

NAME = 'Daily Expense Tracker'
DAILY = 'Daily'
WEEKLY = 'Weekly'
MONTHLY = 'Monthly'
GEO = '720x640+250+150'


def initUI(root):

    # Adding the title to the window
    root.title(NAME)

    # Initilise the Geometry
    root.geometry(GEO)


    # 3 different frames for the menu bar

    top_frame = Frame(root)
    top_frame.pack(fill=BOTH)

    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)


    daily = Button(top_frame, text=DAILY, style="C.TButton").pack(side=LEFT, fill=BOTH, expand=True)

    weekly = Button(top_frame, text=WEEKLY, style="C.TButton").pack(side=LEFT, fill=BOTH, expand=True)

    monthly = Button(top_frame, text=MONTHLY, style="C.TButton").pack(side=LEFT, fill=BOTH, expand=True)

    

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

    # remove maximize/mininize button
    root.resizable(0,0)

    # load the awdark and awlight themes
    root.tk.call("package", "require", 'awdark')
    root.tk.call("package", "require", 'awlight')

    # Initialising Style and loading in a dark thene
    style = Style()
    style.theme_use('awdark')

    #configure buttons
    style.configure("TButton", padding=6, relief="flat")

    # button active/hover tweaks
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

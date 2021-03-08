from tkinter import Tk, BOTTOM, LEFT, RIGHT, CENTER, TOP, BOTH, font, Label, Entry, Listbox, END
from tkinter.ttk import Frame, Style, Button


# Code Constants and variables

NAME = 'Daily Expense Tracker'
DAILY = 'Daily'
WEEKLY = 'Weekly'
MONTHLY = 'Monthly'
GEO = '720x640+250+150'
myfont = 'Vollkorn 16 bold'
menu_font = 'Vollkorn 12 bold'
total = '1,053.00'
theme = '#383c3c'
blue = '#769ddb'
green = '#2ee827'
red = 'red'
number_font = "FontAwesome 16 bold"
tran = 'Vollkorn 14'
stat_font = 'FontAwesome 12 '


def initUI(root):

    # Adding the title to the window
    root.title(NAME)

    # Initilise the Geometry
    root.geometry(GEO)

    # The menu bar frame
    menu_bar(root)
    body(root)


def menu_bar(root):
    # The menu bar frame

    top_frame = Frame(root)
    top_frame.pack(fill=BOTH)

    # The Daily menu button
    Button(top_frame, text=DAILY, style="C.TButton").pack(side=LEFT, fill=BOTH, expand=True)

    # The Weekly menu button
    Button(top_frame, text=WEEKLY, style="C.TButton").pack(side=LEFT, fill=BOTH, expand=True)

    # The Mothly menu button
    Button(top_frame, text=MONTHLY, style="C.TButton").pack(side=LEFT, fill=BOTH, expand=True)

def body(root):

    top_frame = Frame(root)
    top_frame.pack(fill=BOTH)

    # The Balance section

    # The amount number label
    Label(top_frame, text=total,padx=20,pady=20, fg=green, bg='white', font =number_font).pack(side=RIGHT)

    # The currency label
    Label(top_frame, text='Ksh',padx=20,pady=20, fg='white', bg=theme, font=myfont).pack(side=RIGHT)

    # The transactions label
    Label(top_frame, text='Transactions', bg=theme, fg=blue, font=myfont, pady=10).pack(side=LEFT, padx=10)

    scroll(root)


def scroll(root):
    # The middle section full of transactions
    bod = Frame(root)
    bod.pack(fill=BOTH, expand=True)

    # The listbox for the transactions
    mylist = Listbox(bod, font=tran, fg=red)

    # filling the listbox with dummy data

    for i in range(1,26):
        mylist.insert(END, 'Geeks ' + str(i))

    mylist.pack(fill=BOTH,padx=20,pady=10, expand=True)

    # the configuration

    bt_frame(root)



# The Entry frame at the bottom
def bt_frame(root):
    f = Frame(root, padding='0.3i')
    f.pack(side=BOTTOM, fill=BOTH)

    # The input field
    Label(f, text='Enter Amount',padx=10,pady=10, fg='white', bg=theme, font=myfont).pack(side=LEFT)

    Entry(f, font=number_font, justify=CENTER).pack(ipadx = 3, ipady = 8)
     



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
    style.configure("TButton", padding=6, relief="flat", font=menu_font)

    # button active/hover tweaks
    style.map("C.TButton",
    foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', 'gray'), ('active', 'gray')]
    )



def main(root):
    # Add the Theme initilise the UI
    styling(window)
    initUI(window)


# Initialising the window
window = Tk()


#print(font.families())

main(window)
# Starting the mainloop
window.mainloop()
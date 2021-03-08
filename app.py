from tkinter import Tk, BOTTOM, LEFT, RIGHT, CENTER, TOP, BOTH, font, Label, Entry, Listbox, END, StringVar, PhotoImage
from tkinter.ttk import Frame, Style, Button


from time import localtime, asctime

from json import load, dump

# Code Constants and variables


NAME = 'Daily Expense Tracker'
DAILY = 'Daily'
WEEKLY = 'Weekly'
MONTHLY = 'Monthly'
GEO = '720x640+250+150'
myfont = 'Vollkorn 16 bold'
menu_font = 'Vollkorn 12 bold'
total = '0'
theme = '#383c3c'
blue = '#769ddb'
green = '#2ee827'
red = 'red'
number_font = "FontAwesome 16 bold"
tran = 'Gayathri 14'
stat_font = 'FontAwesome 12 '
money = 0

mylist = None
tot = None


'''
This is the 'Backend' of the application. 
'''


# Getting the data from the Json file
def get_data():
    with open('./transactions.json') as f:
        data = load(f)

        # Place the acquired data into variables
        dic = data['Records']
        
        global money 
        money = data['Cash']
    return dic

# Getting the input data ie Cash in hand and the transactions

def get():
    # get the entered amount and set the input field to default
    n = amnt.get()
    amnt.set('')
    t = get_time()

    # create a new dictionary of the entered amount and a timestamp as a key
    record = { f"{t}" : f"{n}"}

    # Append to transactions.json file

    with open('./transactions.json', 'r+') as f:
        data = load(f)
        data['Records'].append(record)

        # Get the new cash after the transaction
        data['Cash'] = str(int(data['Cash']) + int(n))
        
        # set the money variable to the new cash
        global money
        money = data['Cash']

        # move the cursor to the beginning of the file
        f.seek(0)

        # update the data in the file with the new details
        dump(data,f)

    #The decorated string
    string = f"{t}                              {n}"

    # insert the transaction to the UI and the new cash 
    mylist.insert(END,string)
    tot.config(text=str(money))


# getting the time of the transaction
def get_time():
    obj = localtime()
    t = asctime(obj)
    return t




'''
This is the 'Frontend' / UI  of the application. 
'''

# Load all the widgets and window features of the app
def initUI(root):

    # Adding the title to the window
    root.title(NAME)



    # Initilise the Geometry
    root.geometry(GEO)

    # Get the data from the json file
    d = get_data()
    
    # The menu bar frame
    menu_bar(root)
    body(root)
    scroll(root, d)

    # The bottom frame where transaction is added
    bt_frame(root)
 



# The menu of the app
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

# The layout of the body
def body(root):

    top_frame = Frame(root)
    top_frame.pack(fill=BOTH)

    # The Balance section

    # The amount number label
    global tot 
    tot = Label(top_frame,text=money, padx=20,pady=20, fg=green, bg='white', font =number_font)
    tot.pack(side=RIGHT)

    # The currency label
    Label(top_frame, text='Ksh',padx=20,pady=20, fg='white', bg=theme, font=myfont).pack(side=RIGHT)

    # The transactions label
    Label(top_frame, text='Transactions', bg=theme, fg=blue, font=myfont, pady=10).pack(side=LEFT, padx=10)


# The transactions view where  our Json is displayed
def scroll(root, data):
    # The middle section full of transactions
    bod = Frame(root)
    bod.pack(fill=BOTH, expand=True)

    # The listbox for the transactions
    # set the global variable to be equal to the Listbox for global manipulation
    global mylist 

    mylist = Listbox(bod, font=tran, fg='maroon',bg='white')

    # Add the transactions from the json to the listbox
    for i in data:
        for a,b in i.items():
            string = f"{str(a)}                             {b}"
            mylist.insert(END, string)
            
    mylist.pack(fill=BOTH,padx=20,pady=10, expand=True)



# The Entry frame at the bottom that adds to the transactions
def bt_frame(root):
    f = Frame(root, padding='0.3i')
    f.pack(side=BOTTOM, fill=BOTH)

    # The input field
    Label(f, text='Enter Amount',padx=10,pady=10, fg='white', bg=theme, font=myfont).pack(side=LEFT)

    Entry(f, font=number_font, textvariable=amnt, justify=CENTER).pack(side=LEFT, ipadx = 3, ipady = 8)


    Button(f, text='Add', style="C.TButton", command=get).pack(side=LEFT, fill=BOTH, expand=True)

# The styling or the buttons and the theme
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
    
    """)

    # remove maximize/mininize button
    root.resizable(0,0)

    # load the awdark and awlight themes
    root.tk.call("package", "require", 'awdark')
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



# Initialising the window
window = Tk()

amnt = StringVar()


# Add the Theme initilise the UI
styling(window)
initUI(window)

window.mainloop()

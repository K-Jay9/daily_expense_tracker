from tkinter import Tk, BOTTOM, LEFT, RIGHT, CENTER, TOP, BOTH, font, Label, Entry, Listbox, END, StringVar, PhotoImage
from tkinter.ttk import Frame, Style, Button


from json import load, dump

# Importing the utility functions
from utility import  get_time

# Importing the constants
from utility import NAME, DAILY, WEEKLY, MONTHLY, GEO, myfont, menu_font, money, tran, number_font, stat_font, total, theme, blue, green, red
# Code Constants and variables





mylist = None
tot = None

'''
The backend of the application
'''
def get():
    # get the entered amount and set the input field to default
    
    n = amnt.get()
    amnt.set('Enter Amount')

    nt = note.get()
    note.set('Enter Note')
    t = get_time()


    # create a new dictionary of the entered amount and a timestamp as a key
    record = { f"{t}" : [f"{n}", f"{nt}"]}

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
    string = f"{t}      {int(n)}            {nt}"

    # insert the transaction to the UI and the new cash 
    mylist.insert(END,string)
    tot.config(text=str(money))

# Getting the data from the Json file
def get_data():
    with open('./transactions.json') as f:
        data = load(f)

        # Place the acquired data into variables
        dic = data['Records']
        
        global money 
        money = data['Cash']
    return dic



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
            string = f"{str(a)}     {int(b[0])}         {b[1]}"
            mylist.insert(END, string)
            
    mylist.pack(fill=BOTH,padx=20,pady=10, expand=True)



# The Entry frame at the bottom that adds to the transactions
def bt_frame(root):
    f = Frame(root, padding='0.3i')
    f.pack(side=BOTTOM, fill=BOTH)

    # The input field
    g = Entry(f, font=number_font, textvariable=amnt, justify=CENTER)
    g.pack(side=LEFT, padx = 3, ipady=6)

    e = Entry(f, font=number_font, textvariable=note, justify=CENTER)
    e.pack(side=LEFT, padx = 3, ipady=6)


    Button(f, text='Add', style="C.TButton", command=get).pack(fill=BOTH)

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

amnt = StringVar(window, value='Enter Amount')
note = StringVar(window, value='Enter Note')


# Add the Theme initilise the UI
styling(window)
initUI(window)

window.mainloop()

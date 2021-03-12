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


# getting the time of the transaction
def get_time():
    obj = localtime()
    t = asctime(obj)
    return t




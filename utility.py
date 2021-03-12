
from time import localtime, asctime

'''
This file will contain some utility functions and some constants
'''

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



# getting the time of the transaction
def get_time():
    obj = localtime()
    t = asctime(obj)
    return t




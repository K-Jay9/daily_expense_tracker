from time import localtime, asctime
from app import money


def get_time():
    obj = localtime()
    t = asctime(obj)
    print(t)
    return t

print(money)




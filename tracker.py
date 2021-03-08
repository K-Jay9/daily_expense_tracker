from time import localtime, asctime


def get_time():
    obj = localtime()
    t = asctime(obj)
    print(t)
    return t





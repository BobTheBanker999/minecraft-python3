import time

def log(message:str):
    t = ""
    t = t + str(time.localtime().tm_hour) + ":"
    t = t + str(time.localtime().tm_min) + ":"
    t = t + str(time.localtime().tm_sec)
    print("["+t+"][DEBUG]: " + message)

import os
import platform
def deleteAccount():
    try:
        os.system("rm username.txt")
    except:
        os.system("del username.txt")
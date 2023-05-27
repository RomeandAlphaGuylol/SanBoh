from createName import *
from getName import *
from sanboh import *
def check():
    createUserNameFile = open("username.txt", "a")
    openNameFile = open("username.txt", "r").read()
    lines = openNameFile.splitlines()
    if lines==[]:
        print("No Account created .. going to the account creation 'wizard'?")
        name()
        sanboh.main("first")
    else:
        print("Proceeding as it seems you have an account!")
        sanboh.main("I love the letter B/b for some reason :D")
import os
from createName import *
from getName import *
import random
from deleteAccount import *
class sanboh:
    def main(timexd):
        # I didnt got any other param name other than timexd :(
        if timexd=="first":
            print("Well it looks like its your first time here :> have fun!!!!!")
        else:
            print("SanBoh!")
        while True:
            chat = input("Chat with SanBo! -> ")
            if chat.startswith("hi"):
                response_greeting = ["hello there :> Im SanBo! an Idiotic AI!!!", "Hi!", "Hi, Im SanBo an Idiotic AI :D"]
                print(random.choice(response_greeting))
            if chat.startswith("hello"):
                response_greeting = ["hello there :> Im SanBo! an Idiotic AI!!!", "Hi!", "Hi, Im SanBo an Idiotic AI :D"]
                print(random.choice(response_greeting))
            elif chat=="exit":
                quit()
            elif chat.__contains__("my name"):
                try:
                    openUserFile = open("username.txt", "r").read()
                    lines = openUserFile.strip()
                    print(lines)
                except:
                    print("If you have deleted your account! please restart SanBo to take effects")
            elif chat.__contains__("delete"):
                if chat.__contains__("account"):
                    print("Your account has been deleted! please restart SanBo to take effects!")
                    deleteAccount()
            else:
                print("As I said! Im an idiot and I dont seem to know that answer :<")
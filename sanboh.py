import os
from createName import *
from getName import *
import random

class sanboh:
    def main(timexd):
        # I didnt got any other param name other than timexd :(
        if timexd=="first":
            print("Well it looks like its your first time here :> have fun!!!!!")
        else:
            print("SanBoh!")
        while True:
            
            chat = input("Chat with SanBo! -> ")
            if chat.startswith("hello"):
                response_greeting = ["hello there :> Im SanBo! an Idiotic AI!!!", "Hi!", "Hi, Im SanBo an Idiotic AI :D"]
                print(random.choice(response_greeting))
            elif chat=="exit":
                quit()
            else:
                print("As I said! Im an idiot and I dont seem to know that answer :<")
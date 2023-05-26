import os
from createName import *
from getName import *
from sanboh import *
print("SanBoh!")

usernamefile = open("username.txt", "r").read()
if usernamefile==[]:
    name()
else:
    sanboh.main()
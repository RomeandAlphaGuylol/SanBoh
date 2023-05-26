def getUserName():
    usernamefile = open("username.txt", "r").read()
    getName = usernamefile.splitlines()
    print(getName)
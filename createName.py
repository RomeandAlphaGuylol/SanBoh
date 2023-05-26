def name():
    print("Enter your name below!")
    username = input("Your Username: ")
    createUserNameFile = open("username.txt", "w")
    createUserNameFile.write(username)

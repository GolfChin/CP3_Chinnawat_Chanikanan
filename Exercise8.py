usernameInput = input("Username :")
passwordInput = input("Password :")
price = 0
if usernameInput  == "admin"  and passwordInput == "1234":
    print("Welcome",usernameInput)
    print("----- gShop -----")
    print("Computer i7   :25,000")
    print("Notebook i7   :30,000")
    print("Laser Printer : 12,000")
    userSelected = int(input(">>"))
    if userSelected == 1:
        gUnit = input("How many :")
        print("Total is = ",int(gUnit)*25000)
    if userSelected == 2:
        gUnit = input("How many :")
        print("Total is = ",int(gUnit)*30000)
    if userSelected == 3:
        gUnit = input("How many :")
        print("Total is = ",int(gUnit)*12000)
    

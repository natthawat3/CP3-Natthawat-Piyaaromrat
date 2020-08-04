usernameInput = input("Username:")
passwordInput = input("Password:")
applePrice = 10
orangePrice = 5
coconutPrice = 20
mangoPrice = 15

if usernameInput == "tae" and passwordInput == "1234":
    print("Welcome")
    print("---Ko Ko Shop---")
    print("Please select these products below")
    print("1. Apple   @10 THB")
    print("2. Orange  @5  THB")
    print("3. Coconut @20 THB")
    print("4. Mango   @15 THB")
    userSelected = int(input("Select number>>>"))
    if userSelected == 1:
        print("Apple")
        quantity = int(input("Quantity:"))
        print("Total price", applePrice*quantity, "THB")
    elif userSelected == 2:
        print("Orange")
        quantity = int(input("Quantity:"))
        print("Total price", orangePrice*quantity, "THB")
    elif userSelected == 3:
        print("Coconut")
        quantity = int(input("Quantity:"))
        print("Total price", coconutPrice*quantity, "THB")
    elif userSelected == 4:
        print("Mango")
        quantity = int(input("Quantity:"))
        print("Total price", mangoPrice*quantity, "THB")
    else:print("Please check number again.")

else:print("Please check your username and password")
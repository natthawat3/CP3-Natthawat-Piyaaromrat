def login():
    usernameInput = input("Username:")
    passwordInput = input("Password:")
    if usernameInput == "tae" and passwordInput == "1234":
        return showMenu()
    else:
        return False

def showMenu():
    print("Done")
    print("---Ko Ko Shop---")
    print("1. Vat Calculation")
    print("2. Price calculation")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price1 = float(input("First product price"))
        price2 = float(input("Second product price"))
        totalPrice = price1 + price2
        return vatCalculation(totalPrice)
    elif userSelected == 2:
        price1 = float(input("First product price"))
        price2 = float(input("Second product price"))
        totalPrice = price1 + price2
        return priceCalculation(totalPrice)
    else:
        return False

def vatCalculation(totalPrice):
    vat = 7
    result = totalPrice * vat / 100
    return result

def priceCalculation(totalPrice):
    return vatCalculation(totalPrice)+totalPrice

print(login())


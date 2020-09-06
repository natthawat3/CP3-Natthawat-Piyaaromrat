menuList = []
priceList = []

def showInvoice():
    print("-----My food-----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total :", totalPrice)


while True:
    menuName = input("Please enter your menu:")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price:")
        menuList.append(menuName)
        priceList.append(menuPrice)

showInvoice()






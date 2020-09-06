menuList = []

def showInvoice():
    print("-----My food-----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number] [0])
        totalPrice += int(menuList[number] [1])
    print("Total Price:",totalPrice)

while True:
    menuName = input("Please enter your menu:")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price:")
        menuList.append([menuName,menuPrice])

showInvoice()


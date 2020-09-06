menuList = []
systemMenu = {"ข้าวไข่เจียว":30,"ข้าวมันไก่":40,"ข้าวหมกไก่":50,"ข้าวหมูทอด":35}

def showInvoice():
    print("-----My food-----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number] [0],menuList[number] [1])
        totalPrice += int(menuList[number] [1])
    print("Total Price:",totalPrice)

while True:
    menuName = input("Please enter your menu:")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showInvoice()


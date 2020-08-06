totalPrice = int(input("Please fill in the price:"))

def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print(vatCalculate(totalPrice),"THB")
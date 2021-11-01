product = ["Toothpaste", "Soap", "Shampoo"]
catagory = [{"Dabur": 50, "Colgate": 40, "Sensodyne": 60}, {"Lifebuoy": 20, "Khadi": 30, "Wild Stone": 50},
            {"Himalaya": 65, "Sunsilk": 60, "Biotique": 75}]
cart = []
price = []
qnt = []
while (1):
    x = input("press y to enter items into cart or press x to exit")
    if x == "x":
        break
    if x == "y":
        print("Available products are :")
        for i in product:
            print(i)
        p = input("Enter the product name").capitalize()
        indx = product.index(p)
        for i, j in catagory[indx].items():
            print(i, ":", j)
        item = input("enter the catagory name").capitalize()
        qnty = int(input("How many??"))
        cart.append(item)
        price.append(catagory[indx][item] * qnty)
        qnt.append(qnty)
print(cart, price)
print("-------------INVOICE----------------")
for i in range(len(cart)):
    print(qnty, "*", cart[i], "price =", price[i])
print("TOTAL amount : ", sum(price))

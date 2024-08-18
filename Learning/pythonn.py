# 20 Restaurant menus start


class RestaurantTable:

    menus = {
        "pizza":5000,
        "cola":500,
        "apple juice":3000,
        "hamburger":1500,
        "fried potato":3500,
    }

    def __init__(self) :
        self.total =0
        self.orders=[]

    def addOrder(self,order):
        self.orders.append(order)
        self.total+=self.menus[order]

    def printBill(self):
        for order in self.orders:
            print(f"{order}: {self.menus[order]}")

        print(f"total price is {self.total}")

def startProgram():
    table=RestaurantTable()

    while True:
        order=input("order :")
        table.addOrder(order)

        another = input ("order again ? y / n :")
        if another == "y":
            continue;
        if another == "n":
            table.printBill()
            break

startProgram()

prices = [2000,3000,4000,5000]


doublePrices = [];
for price in prices:
    doublePrices.append(price*2)
print(doublePrices);

doublePrices = [price*2 for price in prices ]

print(doublePrices)


# 21 compehension 

nums = [1,2,4,5,6,7,8,64,73,54]
evenD = [num*3 for num in nums if (num%2)==0]
print(evenD);





for num in nums:
    if (num%2)==0 :
        evenD.append(num+10)

print(evenD);

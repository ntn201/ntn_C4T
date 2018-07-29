prices = {}
price_list = [4,2,1.5,3]
for index,fruit in enumerate(["banana", "apple", "orange", "pearl"]):
    prices[fruit] = price_list[index]

stock = {}

stock_list = [6,0,32,15]

for index, fruit in enumerate(prices):
    stock[fruit] = stock_list[index]

for fruit in stock:
    print(fruit,"price: " + str(prices[fruit]), "stock: " + str(stock[fruit]), sep = "\n",end = "\n\n")

total = 0

for fruit in prices:
    fruit_price = stock[fruit]*prices[fruit]
    print("I sold,", stock[fruit], fruit, "for", fruit_price)
    total += fruit_price

print ("Now i have:", total)

# single storage value
num=10

# multi value container
number = [10,20,30]

# read or print values
print(num, type(num), hex(id(num)))
print(number,type(number),hex(id(number)))

# e-commerce problem
#selling price for a single quantity
sellingPriceAmazon = 1500
sellingPriceFlipkart = 1200
print("selling price of amazon:",sellingPriceAmazon, type(sellingPriceAmazon))
print("selling price of flipkart:",sellingPriceFlipkart,type(sellingPriceFlipkart))

profitsAmazon = 3800.33
profitsFlipkart = 4000.12
print(profitsFlipkart,type(profitsAmazon))
print(profitsAmazon,type(profitsFlipkart))

taxes = 18
print(taxes,type(taxes))
# sales of both amazon and flipkart
salesAmazon = [1290,2000,4000]
salesFlipkart = [1240,5000,1000]

totalsalesAmazon = (salesAmazon[0] + salesAmazon[1]+ salesFlipkart[2])*sellingPriceAmazon
print("total sales of amazon-", totalsalesAmazon)

totalsalesFlipkart = (salesFlipkart[0] + salesFlipkart[1] + salesFlipkart[2])*sellingPriceFlipkart
print("total sales of flipkart-", totalsalesFlipkart)

totalProfitsAmazon =  (salesAmazon[0] + salesAmazon[1]+ salesFlipkart[2])*profitsAmazon
print("total profits of amazon",totalProfitsAmazon)
totalProfitsFlipkart = (salesFlipkart[0] + salesFlipkart[1] +salesFlipkart[2])*profitsFlipkart
print("total profits of flipkart", totalProfitsFlipkart)

# check whether amazon or flipkart made more sales
if totalsalesAmazon > totalsalesFlipkart:
    print(" Amazon made more sales")
else:
    print("Flipkart made more sales")
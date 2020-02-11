'''HW2: number
123 -> One
Twenty
Three
'''
number = int(input("enter a number"))
hundredplace = number//100
print(hundredplace)  #1
tensplace = number % 100
print(tensplace)
sum = hundredplace + tensplace
print(sum)
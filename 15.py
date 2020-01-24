# HW1: number 123 -> 1+2+3 -> 6 -> even
#             1*10pow2 + 2*10pow1 + 3*10pow0

number = int(input("enter any number"))

hundredplace = number //100
print(hundredplace)   #1
tensplace = number%100
print(tensplace)   #23
onesplace = tensplace//10
print(onesplace) #2
n1 = tensplace% 10
print(n1)    #3
sum  = hundredplace + onesplace + n1
print(sum)

if (sum%2) ==0:
    print("even")
else:
    print("odd")
#container creation
age = 10
'''print("age-",age, type(age),hex(id(age)))
print("age-",age, type(age),oct(id(age)))
print("age-",age, type(age),bin(id(age)))
'''
joesAge = 20
print("joe age",joesAge,id(joesAge))

loveAge = 19
print("love age",loveAge, id(loveAge))

del age
#print("age-",age, type(age),hex(id(age))) ---- error

del loveAge
#print("love age",loveAge, id(loveAge)) ---- error
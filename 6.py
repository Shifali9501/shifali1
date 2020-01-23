name="john watson"
print(max(name))
print(name[1])
print(name[len(name)-1])

print(name[1:4])
print(name[1], name[-2])

print(name[::-1])

email= input("enter your email")
print("email is", email)
if '@' in email and '.' in email:
    print("valid email")
else:
    print("invalid email")



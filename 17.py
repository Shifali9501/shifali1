employee={
    "name" : "john",
"eid":101,
"salary" : 3000,
"rating" : 4.5
}
print(employee,len(employee))
print(max(employee))
print(min(employee))

employee["name"] ="john watson"
print(employee)

del employee["eid"]
print(employee)

keys = employee.keys()
values = employee.values()
print(keys, type(keys))
print(values,type(values))
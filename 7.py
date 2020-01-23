'''# strings are immutable
name="Fionna Flyn"
print("name is, name")
newName = name.upper()
print("name now is", newName)

authorname = "john watson"
print(authorname,hex(id(authorname)))
newauthorname = authorname.capitalize()
print(newauthorname, hex(id(newauthorname)))

names="john, jenny, jack, joe"
print(names[0])
print(names[len(names)-1])

num = names.count("j", 0, len(names))
print(num  )
'''
quotes = """Work hard, get luckier
search the candle rather than cursing the darkness
"""
def count(data, word, start, end):
    c=0
    j=0

    return c
for i in range(start,end):
    print(data[i] == word[j])


print("the occurs ", count(quotes, "the", 0,  len(quotes)))

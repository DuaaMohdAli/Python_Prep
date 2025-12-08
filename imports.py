from math import sqrt , pi

print(sqrt(16))
print(pi*2)



import random 

number = random.randint(1,10)
print(number)

fruits = random.choice(["apple" , "banana" , "kiwi"])
print(fruits)



import json
data = {"name" : "Duaa" , "age" : 20}

json_strings = json.dumps(data)

print(json_strings)
import json

numbers = [1,2,3,4,4,4,4,4,4,4]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

Your_name=input("What's your name?")
print("I know your name is "+Your_name)
your_name=Your_name
file='name.jason'
with open(file,'w') as n:
    json.dump(your_name,n)
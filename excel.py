import pandas as pd
import numpy as np
Path="a.csv"
data1= {
    "name":["WT","WTT"],"age":[10,20]
}
data2={
    "name":["A","B","C"],"age":[22,33,44]
}
df1=pd.DataFrame(data=data1)
df2=pd.DataFrame(data=data2)
df3=df1.merge(df2,how='outer')
df4=pd.concat([df1,df2],sort=True)
# df.to_csv(Path,index=False)
print(df3)
print(df4)
a="miscellaneous"
print(str.upper(a))
df5=pd.read_excel("courses.xlsx")
print(df5)
a=np.array([2,5,1,6,8,1.5])
print(np.sort(a))
# S1=pd.Series(['a','b'])
# S2=pd.Series(['c','d'])
# print(pd.concat([S1,S2],ignore_index=True))
# print(df2)
# print(df.pivot(index='age',columns='name'))

wt=[1,2,3,4,5]
print(wt[-1])
print(wt.pop())

# name=['Tom',2,3,4,5,6,7,1,2,3,4,3]
# len=len(name)
# print("len="+str(len))
# print(name[range(1,len)])

squares=[]
for i in range(1,12):
    square=i**2
    squares.append(square)
print(squares)
squares1=[square1**2 for square1 in range(1,12)]
print(squares1)

odd_number_coll=[]
even_number_coll=[]
for number in range(1,20):
    if number % 2 == 1:
        odd_number_coll.append(number)
    elif number % 2 ==0:
        even_number_coll.append(number)

print(odd_number_coll)
print(even_number_coll)

print(2%2)
print(squares[::-1])


banned_users = ['andrew', 'carolina', 'david']
user = 'Rex'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


age = int(input("age="))
if age > 18:
    print("You are a man")
elif age > 6:
    print("You are a teen")
else:
    print("You are a child")


wang = {"name":"rex","color":"red"}
wang["height"] = 20
print(wang)

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():
    print(name.title())
for values in favorite_languages.values():
    print(values)
aliens=[]
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)
print(len(aliens))
df=pd.DataFrame(aliens)
print(df)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        print(alien)
# df.to_excel("test.xlsx")
# abc=[]
# for copy in range(280):
#     copy1 = {"excel":""}
#     abc.append(copy1)
# df1 = pd.DataFrame(abc)
# df1.to_excel("test1.xlsx")
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)



users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
},
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
},
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
print(f"\tFull name: {full_name.title()}")
print(f"\tLocation: {location.title()}")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
# df7=pd.DataFrame(user_profile)
# df7.to_csv('wt.csv',index=True)
print(user_profile)


def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car_profile = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car_profile)


def add(a,b=3):
    return a+b


class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
class Cat:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fight(self):
        print(f"{self.name} was fighting with {my_dog.name}")
my_cat = Cat('Rex',1)
my_cat.fight()

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
my_car=Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())
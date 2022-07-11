import pandas as pd
import numpy as np
import random
import json
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
# df5=pd.read_excel("courses.xlsx")
# print(df5)
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

'''
age = int(input("age="))
if age > 18:
    print("You are a man")
elif age > 6:
    print("You are a teen")
else:
    print("You are a child")
'''

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
        self.odometer_reading = 100

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""

        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""

        # self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\nYou can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_car=Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())
# my_car.update_odometer(23500)
# my_car.read_odometer()
# my_car.increment_odometer(100)
# my_car.read_odometer()
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        self.battery_size=75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def battery_update(self,size):
        self.battery_size += size

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""

        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery_update(10)
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

# battery_size1=int(input("battery_size="))
class Battery:
    # battery_size1 = input("battery_size=")
    # def __init__(self,battery_size=battery_size1):
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""

        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class Luxury_Car(Car):  #second Car: Parent Class
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
mybmw=Luxury_Car("BMW","X6",2022)
print(mybmw.get_descriptive_name())
mybmw.battery.describe_battery()
mybmw.battery.get_range()

print(random.randint(1,6))
Path = 'D:/配置文档/pi_digits.txt'

with open(Path) as file_object:
    # contents=file_object.read()
    # for line in contents:
    #     print(line)
    lines=file_object.readlines()
    pi_string = ''
    for line in lines:
        # print(line.rstrip())
        # pi_string+=line.rstrip()
        pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))
# print(contents.rstrip()) # 删除尾部字符space

new_filename='pi_million_digits.txt'
with open(new_filename) as new_file_object:
    new_lines=new_file_object.readlines()
    new_pi_string=''
    for new_line in new_lines:
        new_pi_string += new_line
    # birthday = input("Enter your birthday, in the form mmddyy: ")
    # if birthday in new_pi_string:
    #     print("Your birthday appears in the first million digits of pi!")
    # else:
    #     print("Your birthday does not appear in the first million digits of pi.")
    print(f"{new_pi_string[:3]}...")
    print(len(new_pi_string))

filename='programming.txt'
with open(filename, 'w') as write_object:
    write_object.write("I love programming.")
    write_object.write("I love creating new games.")
with open(filename,'a') as add:
    add.write("\nREXERXERX"*10)
print("aa"*7)
try:
    print(5/0)
except ZeroDivisionError:
    print("0 can't be divided")


'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
        # print(answer)
    except ZeroDivisionError:
        print("Please re-input again correctly")
    else:
        print(answer)
'''




filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
    # print(contents)
except FileNotFoundError:
    # f.write("Rex is God")
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

Rex="Rex is God"
print(Rex.split())
print(len(Rex.split()))

def count_words(new_filename):
    try:
        with open(new_filename, encoding='utf-8') as f:
            contents = f.read()
        # print(contents)
    except FileNotFoundError:
        # f.write("Rex is God")
        pass
        # print(f"Sorry, the file {new_filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {new_filename} has about {num_words} words.")

count_words('alice.txt')


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

line_wt = "Row, row, row your boat"
print(line_wt.count('row'))
print(line_wt.lower().count('row'))

# numbers=[1,2,3,4,5,6,7,8,9,11]
Rex_filename = 'numbers.json'
Rex_file='name.json'
RRex_file='nname.json'
# with open(Rex_filename, 'w') as f:
#     json.dump(numbers, f)
with open(Rex_filename) as r:
    new_numbers = json.load(r)
print(new_numbers)

with open(Rex_file) as o:
    new_name = json.load(o)
    print("Welcome back: "+new_name)

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
def get_store_username():
    """Get stored username if available."""
    filename = RRex_file #参考428
    try:
        with open(RRex_file) as ff:
            username = json.load(ff)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    # filename = 'nname.json'
    with open(RRex_file, 'w') as f:
        json.dump(username, f)
        return username

def greet_user():
    """Greet the user by name."""
    username=get_store_username()
    if username:
        print(f"2nd Welcome back, {username}!")
    else:
        # username = input("What is your name? ")
        # my_name = RRex_file #参考428
        # with open(my_name, 'w') as f:
        #     json.dump(username, f)
        get_new_username()
        print(f"2nd We'll remember you when you come back, {username}!")
    # my_name = 'name.json'
    # try:
    #     with open(my_name) as f:
    #         username = json.load(f)
    # except FileNotFoundError:
    #     username = input("What is your name? ")
    #     with open(my_name, 'w') as f:
    #         json.dump(username, f)
    #         print(f"We'll remember you when you come back, {username}!")
    # else:
    #     print(f"Welcome back, {username}!")
# get_new_username()
greet_user()


import unittest
from name_function import get_formatted_name
from name_function import add
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
    def test_add(self):
        add_result=add(4,9)
        self.assertIn(add_result,[1,2,3,4,5])

    def test_addd(self):
        addd_result=add(5,1)
        self.assertIn(addd_result,[6,7])

if __name__ == '__main__':
    unittest.main()



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
# df.to_excel("test.xlsx")
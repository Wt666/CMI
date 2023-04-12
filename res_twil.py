# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
#
#
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['ACbd979f76fbcff11505f6b5a568eb9161']
# auth_token = os.environ['81178896371d5a4c6d35e0b77183d6ac']
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#     .create(
#          messaging_service_sid='SMbb07878fbed1f987c7a22785427a1036',
#          body='body',
#          to='+18573361164'
#      )
#
# print(message.sid)

if any([True,False,False]) == True:
    print("Yes")

college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
print(list(enumerate(college_years, 2019)))

class my_secrets:
    def __init__(self, password):
        self.password = password
        pass
instance = my_secrets('1234')
print(instance.password)

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')
D = Student('Rex',1,1)

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
print(D.name)

import math
radius = [1,2,3]
area = list(map(lambda x: round(math.pi*(x**2), 2), radius))
print(area)
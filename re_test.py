import re

line = "https://bit.ly/*aB*nyg"

# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# matchobj=re.match(r'สินเชื่อ.*')

# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
m = re.findall(r'(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-zA-Z0-9]+([-.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?', line)

if m:
    print("Match")
    print(m)

else:
    print("No Match!!")


a=5
b=6
if a <b:
    print(True)

num=[];
i=2
for i in range(2,74):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num.append(i)

print(num)
import random
import string


def GenPassword(length):
    chars = string.ascii_letters + string.digits
    return "".join(([random.choice(chars) for i in range(length)]))
    # return "".join(random.sample(chars, 8))


password = []
if __name__ == "__main__":
    for i in range(4):
        # password.append(GenPassword(8))
        print(GenPassword(8))
        password.append(GenPassword(8))
    print(password)

print(hex(69))
str1 = '0x{:02X}'.format(69)
str2 = '0x{:02X}'.format(15)
print(str1, str2)

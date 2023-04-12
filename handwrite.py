import pywhatkit

# print(pywhatkit.text_to_handwriting('''Learning Python from the basics is extremely important. Before starting to learn python,understanding a base language like c is a must and some of the oops concepts.Python program has many modulesand packages, which helps with efficient programming.
# Understanding these modules and 1proper usage of many syntax and libraries is recommended.
# In this article, a few modules and packages are used in the program.
# Python includes tons of libraries and some of them are quiet intresting'''))

import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+85269044836",
            message=msg,
            tab_close=True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    send_whatsapp_message(msg="Test message from a Python script!")
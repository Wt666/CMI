from wxpy import *

bot=Bot()
my_friend=bot.friends().search('byoobiu',sex=FEMALE)[0]

my_friend.send('Hello')
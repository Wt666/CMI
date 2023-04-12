import requests

# 输入成本C（HKD）和收入R（CNY）
C = float(input("请输入成本(HKD)："))
R = float(input("请输入收入(CNY)："))

# 获取汇率API返回的当日汇率
response = requests.get("https://api.exchangerate-api.com/v4/latest/CNY")
exchange_rate = response.json()["rates"]["HKD"]

# 计算交易利润P
P = ((R * exchange_rate) - C)/ exchange_rate
P_HKD = P * exchange_rate
# 输出当日汇率和交易利润P，单位为CNY
print("当日汇率为：1 CNY = %.2f HKD" % exchange_rate)
print("交易利润为：%.2f CNY" % P)
print("交易利润为：%.2f HKD" % P_HKD)

# import turtle

# # 创建一个turtle对象
# star = turtle.Turtle()
#
# # 设置线条宽度和颜色
# star.pensize(5)
# star.color("red")
#
# # 向前移动一段距离，然后向左旋转144度
# # 重复五次，以形成五角星的形状
# for i in range(5):
#     star.forward(200)
#     star.left(144)
#
# # 关闭turtle窗口
# turtle.done()
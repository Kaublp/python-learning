import random
lucky_number = random.randint(1,10)
print("抽奖游戏开始!!!!!!!")
inter_number = int(input("请输入您心仪的数字："))
if lucky_number == inter_number:
    print("恭喜恭喜恭喜您，中中中中中大奖啦！！！！！！")
elif lucky_number != inter_number:
    print(f"很很很遗憾呢，您没中奖，中奖数字为{lucky_number}")
elif inter_number <1 or inter_number > 10:
    print("您输入的数字不对呢")
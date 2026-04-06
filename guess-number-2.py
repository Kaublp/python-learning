import random

secret = random.randint(1,100)
chances = 7

print("猜数字游戏开始")
print(f"你有{chances}次机会尝试猜1-100之间的数字")

for i in range(chances):
    guess = int(input(f"第{i+1}次猜数字："))
    if guess == secret:
        print(f"恭喜，第{i+1}次就猜对了")
        print(f"游戏结束，答案为{secret}")
        break
    elif guess > secret:
        print("猜大了")
    else:
        print("猜小了")

    left = chances - i - 1

    if left > 0:
        print(f"还有{left}次机会")

    else:
        print(f"游戏结束，答案为{secret}")

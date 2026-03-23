import sys
password = 123456
have_money = 5672
yes = "是"
while(True):
    inter_password = int(input("请输入您的密码："))
    if password == inter_password:
        break
    else:
        print("您输入的密码错误，是否继续取款，是/否")
        anwser = input()
        if anwser == "是":
            continue
        else :
            print("您的取款已结束")
            sys.exit()
while(True):
    out_money = int(input("请输入您要取的金额："))
    if out_money > have_money:
        print("您的余额不足,请重新输入")
        continue
    else:
        newhave_money = have_money - out_money
        print(f"您的取款已结束，您的余额为{newhave_money}")
        break
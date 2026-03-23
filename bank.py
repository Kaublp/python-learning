import sys
#请设置您的信息
password = int(input("请输入您设置的密码:"))
have_money = float(input("请输入您设置的余额:"))
print("-----------------------------------")
#程序开始
while True :
    inter_password = int(input("请输入您的密码："))
    #验证密码
    if password == inter_password:
        print("输入正确，请继续取款")
        print("-----------------------------------")
        break
    else:
        #询问是否继续取款
        print("您输入的密码错误，是否继续取款，是/否")
        anwser = input()
        if anwser == "是":
            continue
        else :
            print("您的取款已结束")
            print("-----------------------------------")
            sys.exit()
while True:
    out_money = float(input("请输入您要取的金额："))
    if out_money > have_money:
        print("您的余额不足,请重新输入")
        continue
    else:
        new_money = have_money - out_money
        print(f"您的取款已结束，您的余额为{new_money}")
        print("-----------------------------------")
        break
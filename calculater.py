print("请输入第一个数字：")
num1 = int(input())
print("请输入第二个数字：" )
num2 = int(input())
print("请输入运算符（*，-，+，/）：")
operator = input()
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    while True:
        if num2 == 0:
            print("您输入的0不可以做除数，请重新输入：")
            num2 = int(input())
            continue
        else:
            print(num1 / num2)
            break
else:
    print("您输入的运算符是无效的")
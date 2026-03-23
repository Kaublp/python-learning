# # num1 = int(input("请问您要摄氏度转华氏度：1/华氏度转摄氏度：2  ：\n"))
# # num2 = int(input("请输入您要转化的温度："))
# # if num1 == 1:
# #     num3 = int(num2 * 9/5) + 32
# #     print("华氏度为" , num3)
# # if num1 == 2:
# #     num3 = int(num2 -32) * 5/9
# #     print("摄氏度为：" , num3)
#
#
# while(True):
#     num = int(input ("请输入数字（1-7）：\n"))
#     if num == 1 :
#         print("今天星期一")
#     elif num == 2 :
#         print("今天星期二")
#     elif num == 3 :
#         print("今天星期三")
#     elif num == 4 :
#         print("今天星期四")
#     elif num == 5 :
#         print("今天星期五")
#     elif num == 6 :
#         print("今天星期六")
#     elif num == 7 :
#         print("今天星期七")
#     else:
#         print("无效")
#
#     answer = int(input("是否继续查询是1否2\n"))
#     if answer == 1:
#         continue
#     elif answer == 2:
#         break


import random
num1 = int(input("请输入您的数字:"))
num2 = random.randint(1,10)
if num1 == num2:
    print("恭喜您中奖了")
else:
    print("谢谢惠顾")
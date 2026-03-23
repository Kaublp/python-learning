print("请输入您要查询的年份：")
a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 ==0:
    print(a , "是闰年")
else:
    print(a , "不是闰年")
score = int(input("请输入分数（0-100）："))

if score < 0 or score > 100:
    print("无效分数")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
print("摄氏度转华氏度:1")
print("华氏度转摄氏度:2")
choice = input("请输入1/2\n")
temperature = float(input("请输入温度"))
if choice == "1":
    new_temperature = temperature * 1.8 + 32
    print(f"{temperature}C = {new_temperature}F")
elif choice == "2":
    new_temperature = (temperature - 32) / 1.8
    print(f"{temperature}F = {new_temperature}C")
else:
    print("无效选择")
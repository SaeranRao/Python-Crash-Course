print("请输入两个数字，我会给予除法结果")
print("输入'q'退出。")

while True:
    first_number = input("请输入第一个数字：")
    if first_number == 'q':
        break
    second_number = input("请输入第二个数字：")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print(f"第二个数字为零，请重新输入，输入 q 退出计算。")
    else:
        print(f"{first_number} 除以 {second_number} 的结果为{answer}")
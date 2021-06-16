from name_function import get_formatted_name

print("输入 q 即可退出")
while True:
    first = input("请输入姓\n")
    if first == 'q':
        break
    last = input("请输入名\n")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(f"你的名字是：{formatted_name}")
filename = 'F:\\Python\\Python编程从入门到实践\\10\\text_files\\programming.txt'
with open(filename,'a') as file_object:
    file_object.write(input("请输入要记录的话！\n")+"\n")
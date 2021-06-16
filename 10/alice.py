filename = 'F:\\Python\\Python编程从入门到实践\\10\\text_files\\alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("不好意思，文件不存在")
    

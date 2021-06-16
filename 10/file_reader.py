file_path = 'F:\\Python\\Python编程从入门到实践\\10\\text_files\\pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
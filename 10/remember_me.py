import json

def get_stored_username():
    filename = '10\\json_files\\username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("请输入你的用户名~")
    filename = '10\\json_files\\username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"{username}欢迎回来~")
    else:
        username = get_new_username()
        print(f"我们已经记录了您的名字，欢迎光临~ {username}")
        
greet_user()
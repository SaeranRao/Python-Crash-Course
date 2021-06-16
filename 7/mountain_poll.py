responses = {}
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\n请问你叫什么名字？")
    response = input("请问你想去爬哪座山？")
    responses[name] = response
    repeat = input("是否还有别的朋友要参加调研？（是/否）")
    if repeat == '否':
        polling_active = False
print("\n-------调查结果--------")
for name,response in responses.items():
    print(f"{name}想去爬{response}")
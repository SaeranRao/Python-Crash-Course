#首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
#模拟打印每个设计，知道没有未打印的设计为止
#打印每个设计后，都将其移到列表completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"正在打印的设计为：{current_design.title()}")
    completed_models.append(current_design)

for design in completed_models:
    print(design.title())
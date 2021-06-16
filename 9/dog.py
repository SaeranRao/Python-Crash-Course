class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name}正蹲着！")

    def roll_over(self):
        print(f"{self.name}正在打滚！")

Dog1 = Dog('阿黄',18)
# Dog1.sit()
# Dog1.roll_over()
print(Dog1.name.title())
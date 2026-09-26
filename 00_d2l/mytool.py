def add(a,b):
    return a+ b

class Calculator:
    def __init__(self,name):
        self.name = name

    def multiply(self,a,b):  #self的作用是让方法知道我现在在操作哪个对象
        print(self.name)
        return a * b 
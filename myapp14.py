#クラス変数

class User:
    #クラス変数
    count = 0
    def __init__(self,name):
        User.count +=1
        self.name = name
print(User.count) #0
tom = User("tom")
bob = User("bob")
print(tom.name)
print(bob.name)
print(tom.count)
print(User.count) #1


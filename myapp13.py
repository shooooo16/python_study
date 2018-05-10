#コンストラクタ
class User:
    def __init__(self,name):
        self.name = name

tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)

input1 = input("ユーザー名を入力してください")

inputuser = User(input1)
print(inputuser.name)

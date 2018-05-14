#Userモジュール

class User:
    count=0
    def __init__(self,name):
      User.count += 1
      self.name = name
    #インスタンスメソッド
    def say_hi(self):
        print("hi {0}" .format(self.name))
class AdminUser(User):
    def __init__(self,name,age):
        #super().__init__(name)
        self.name = name
        self.age = age
    def say_hello(self):
        print("hello {0} ({1})" .format(self.name,self.age))
    #override
    def say_hi(self):
        print("(admin)hi {0}" .format(self.name))
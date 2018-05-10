#メソッド(クラス内に定義された関数)
class User:
    count=0
    def __init__(self,name):
      User.count += 1
      self.name = name
    #インスタンスメソッド
    def say_hi(self):
        print("hi {0}" .format(self.name))
    #クラスメソッド
    @classmethod
    def show_info(cls):
        print("{0} instances" .format(cls.count))

tom = User("tom")
bob = User("bob")
tom.say_hi()
User.show_info()

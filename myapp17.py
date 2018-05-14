#クラスの多重継承

class A:
    def say_a(self):
        print("a!")
    def say_hi(self):
        print("Hello form a")

class B:
    def say_b(self):
        print("b!")
    def say_hi(self):
        print("Hello form b")
class C(B,A):
    pass
    
c = C()
c.say_a()
c.say_b()
c.say_hi()


#関数

def say_hello():
    print("hello")

def say_information(name,age=20):
    print("hi {0} ({1})" .format(name,age))

say_hello()
say_information("tom",23)
say_information("mike",28)
say_information("steave")
say_information(age = 18,name = "george")

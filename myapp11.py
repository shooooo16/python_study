#変数のスコープ

def say_hi():
    msg = "hi" #ローカル変数
    print(msg)
    
msg = "hello" #グローバル変数

say_hi()   #hi
print(msg) #hello


msg = "hello global"
def say_global():
    global msg
    msg = "hello global2"
    print(msg)

say_global() #hello global2
print(msg) #hello global2

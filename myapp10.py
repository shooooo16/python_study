#関数の返り値

def say_hi():
    return "hi"
    print("hello") #returnのため表示されない
    
msg = say_hi()
print(msg)

def pass_test():
    pass #関数の中身が無記入の場合、エラーが起きる
    
msg = pass_test()
print(msg)

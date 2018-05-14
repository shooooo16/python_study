#例外処理

class MyException(Exception):
    pass

def div(a,b):
    try:
        if b < 0:
            raise MyException("マイナスでは割れません")
        print(a / b)
    except ZeroDivisionError:
        print("0では割れません")
    except MyException as e:
        print(e)
    else:
        print("例外なし")
    finally:
        print("--end--")
div(10,2)
div(10,0)
div(10,-3)

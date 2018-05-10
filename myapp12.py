#クラス

class User: #クラス名の一文字目は大文字
    pass

tom = User() #インスタンス
tom.name = "tom"
tom.score = 78

mike = User() #インスタンス
mike.name = "mike"
mike.level = 5

print(tom.name)
print(mike.level)
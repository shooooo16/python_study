#イテレータ

scores = [40,50,70,90]

it = iter(scores)

print(next(it))
print(next(it))
print("Hello")
print(next(it))


for score in scores:  #自動的にイテレータを使用している
    print(score)


def get_infinite(): #イテレータを作る関数をジェネレータと呼ぶ
    i = 0
    while True:
        yield i * 2
        i += 1
g = get_infinite()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

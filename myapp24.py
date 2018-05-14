#集合型（セット）-重複を許さない

a = set([5,4,8,5])
b={5,4,8,5}

print(a)
print(b)

flg = 5 in a
print(flg)

a.add(2)
print(a)
print(len(a))

a.remove(4)
print(a)
print(len(a))

c = {1,3,5,8}
d = {3,5,8,9}

print(c | d) #和集合 1,3,5,8,9
print(c & d) #積集合 3,5,8
print(c - d) #差集合 1
print(d - c) #差集合 9

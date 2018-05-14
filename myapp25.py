#辞書型

sales = {"taguchi":400, "koji":400}
print(sales["taguchi"])
sales["taguchi"] = 500
sales["imai"] = 250
print(sales)
del(sales["koji"])
print(sales)

for key,value in sales.items():
    print("{0} → {1}" .format(key,value))
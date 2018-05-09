# if

score = int(input("得点を入力してください"))

if score >80:
    print("Great!")
elif score >=60:
    print("Good")
else:
    print("So so")	


score = int(input("得点を入力してください2"))
print("Great!" if score >80  else "Soso")


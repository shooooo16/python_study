#リスト型

scores = [40,50]
print(scores[0])
print(len(scores))
scores[0] = 45
print(scores[0])
scores.append(65)
print(len(scores))
print(scores)

for score in scores:
    print(score)

for i,score in enumerate(scores):
    print("{0}は{1}" .format(i,score))

N = int(input())
results = []
score = 0
for i in range(N):
    s = input()
    point = 0
    for c in s:
        if c == 'X':
            point = 0
        else:
            point += 1
        score += point
    results.append(score)
    score = 0

for i in results:
    print(i)

x, y, w, h = map(int, input().split())

a = x if x < w/2 else w-x
b = y if y < h/2 else h-y
ans = a if b > a else b
print(ans)

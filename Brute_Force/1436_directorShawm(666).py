def movie_number(n):
    i = 0
    num = 666
    while True:
        if str(num).find('666') != -1:
            i += 1
        if i == n:
            break
        num += 1
    return num

if __name__ == '__main__':
    N = int(input())
    print(movie_number(N))
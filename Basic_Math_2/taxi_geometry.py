import math


def Euclidean(r):
    return r*r*math.pi


def TaxiCab(r):
    return 2*r*r


def main():
    r = int(input())
    print('{:.6f}'.format(Euclidean(r)))
    print('{:.6f}'.format(TaxiCab(r)))


if __name__ == '__main__':
    main()

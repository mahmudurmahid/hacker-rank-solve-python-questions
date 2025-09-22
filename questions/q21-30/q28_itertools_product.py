from itertools import product

def itertools_prod():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = product(A, B)
    print(*result)

itertools_prod()
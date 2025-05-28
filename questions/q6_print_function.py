from __future__ import print_function

def print_function(n):
    for i in range(1, n + 1):
        print(i, sep='', end='')

n = 5
result = print_function(n)
print(result)

# if __name__ == '__main__':
#     n = int(input())
#     print_function(n)
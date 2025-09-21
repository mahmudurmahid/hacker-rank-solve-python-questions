def cuboid_values(x, y, z, n):
    all_sequences = [[i, j, k] for i in range(x + 1)
                                for j in range(y + 1)
                                for k in range(z + 1)]

    valid_sequences = [sequence for sequence in all_sequences 
                       if (sequence[0] + sequence[1] + sequence[2]) != n]

    return valid_sequences

def alt_cuboid_values(x, y, z, n):
    sequences = [[i, j, k] for i in range(x + 1)
                            for j in range(y + 1)
                            for k in range(z + 1)
                            if (i + j + k) != n]

    return sequences

x = 1
y = 1
z = 2
n = 3
result = cuboid_values(x, y, z, n)
print(result)
alt_result = alt_cuboid_values(x, y, z, n)
print(alt_result)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     print(cuboid_values(x, y, z, n))
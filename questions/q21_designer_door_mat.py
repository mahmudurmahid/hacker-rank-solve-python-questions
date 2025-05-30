def designer_door_mats(n, m):
    # Top half
    for i in range(1, n, 2):
        pattern = (".|." * i).center(m, "-")
        print(pattern)

    # Center line with "WELCOME"
    print("WELCOME".center(m, "-"))

    # Bottom half
    for i in range(n - 2, 0, -2):
        pattern = (".|." * i).center(m, "-")
        print(pattern)

n = 9
m = 27
result = designer_door_mats(n, m)
print(result)
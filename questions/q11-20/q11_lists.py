def lists(n):
    options = []

    for i in range(n):
        options.append(i)

    new_list = []
    new_list.append(options[1])
    new_list.append(options[2])
    new_list.insert(1, options[3])

    return new_list

n = 4
result = lists(n)
print(result)
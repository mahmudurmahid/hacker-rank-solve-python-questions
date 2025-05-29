def split_and_join(line):
    split_line = line.split(" ")
    joint_line = "-".join(split_line)

    return joint_line

s = "this is a string"
result = split_and_join(s)
print(result)
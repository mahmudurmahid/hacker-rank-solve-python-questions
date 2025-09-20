def split_and_join(line):
    split_line = line.split(" ")
    joint_line = "-".join(split_line)

    return joint_line

def alt_split_and_join(line):
    final_line = "-".join(line.split(" "))

    return final_line

s = "this is a string"
result = split_and_join(s)
print(result)
alt_result = alt_split_and_join(s)
print(alt_result)
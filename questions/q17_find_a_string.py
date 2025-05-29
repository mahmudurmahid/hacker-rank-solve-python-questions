def count_substring(string, sub_string):
    count = 0

    # loop through all possible positions in the string where the substring could start (i.e string[0] - string[4] for this example)
    for i in range(len(string) - len(sub_string) + 1):
        # check if the slice of the original string at position i:length of sub_string is equal to sub_string
        if string[i:i+len(sub_string)] == sub_string:
            count += 1

    return count

string = "ABCDCDC"
sub_string = "CDC"
result = count_substring(string, sub_string)
print(result)
import textwrap

def wrap(string, max_width):
    fill = textwrap.fill(string, max_width)
    return fill

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
result = wrap(string, max_width)
print(result)
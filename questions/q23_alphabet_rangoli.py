import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabet[size-1:i:-1] # ascending characters
        center = alphabet[i]        # center character
        right = alphabet[i+1:size]  # descending characters
        
        row = '-'.join(left + center + right)
        line = row.center(4*size - 3, '-') # (4*size - 3, '-') provides each line's width symetrically
        lines.append(line)

    full_pattern = lines[:size-1][::-1] + lines

    return '\n'.join(full_pattern)


size = 5
result = print_rangoli(size)
print(result)
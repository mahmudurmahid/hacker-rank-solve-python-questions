def print_formatted(number):
     # convert number to a binary string; [2:] removes '0b' prefix from binary string
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # rjust(width) pads the number with spaces on the left to make total length equal to width
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
    
        print(decimal, octal, hexadecimal, binary)

number = 17
result = print_formatted(number)
print(result)
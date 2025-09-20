def str_validators(s):
    print(any(char.isalpha() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

def alt_str_validators(s):
    alphanumeric_condition = False
    alphabetical_condition = False
    digit_condition = False
    lowercase_condition = False
    uppercase_condition = False

    for i in s:
        if i.isalnum():
            alphanumeric_condition = True
        if i.isalpha():
            alphabetical_condition = True
        if i.isdigit():
            digit_condition = True
        if i.islower():
            lowercase_condition = True
        if i.isupper():
            uppercase_condition = True

    print(alphanumeric_condition)
    print(alphabetical_condition)
    print(digit_condition)
    print(lowercase_condition)
    print(uppercase_condition)

s = "qA2"
result = str_validators(s)
print(result)
alt_result = alt_str_validators(s)
print(alt_result)
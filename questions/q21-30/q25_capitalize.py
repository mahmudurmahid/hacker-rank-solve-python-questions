def solve(s):
    capitalized_name =  ' '.join(name.capitalize() for name in s.split(' ')) 

    return capitalized_name


def alt_solve(s):
    capitalized_name = s.split(" ")

    new_name = ""

    for name in capitalized_name:
        new_name += name.capitalize() + " "
    
    return new_name

s = "chris alan"
result = solve(s)
print(result)
alt_result = alt_solve(s)
print(alt_result)
def solve(s):
    capitalized_name =  ' '.join(name.capitalize() for name in s.split(' ')) 

    return capitalized_name

s = "chris alan"
result = solve(s)
print(result)
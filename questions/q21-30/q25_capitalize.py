def solve(s):
    capitalized_name =  ' '.join(word.capitalize() for word in s.split(' ')) 

    return capitalized_name

s = "chris alan"
result = solve(s)
print(result)
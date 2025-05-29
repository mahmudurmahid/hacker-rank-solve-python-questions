def swap_case(s):
    changed_case = s.swapcase()
    return changed_case

def alt_swap_case(s):
    return s.swapcase()

s = 'HackerRank.com presents "Pythonist 2".'
result = swap_case(s)
print(result)
alt_result = alt_swap_case(s)
print(alt_result)
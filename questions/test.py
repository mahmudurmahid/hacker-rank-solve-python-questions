def minimum_swaps(s):
    balance = 0       # difference between '(' and ')'
    extra_close = 0   # count of unmatched ')'

    for i in s:             # <--- using for i in s
        if i == '(':
            balance += 1
        else:  # i == ')'
            if balance > 0:
                balance -= 1
            else:
                extra_close += 1   # this ')' has no matching '('

    # each swap fixes two misplaced brackets
    return (extra_close + 1) // 2


s = "(()))())"
result = minimum_swaps(s)
print(result)
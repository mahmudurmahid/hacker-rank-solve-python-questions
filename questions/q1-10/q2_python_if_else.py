def weird_or_not(n):
    if (n % 2 != 0) or (n % 2 == 0 and 6 <= n <= 20):
        answer = "Weird"
    elif (n % 2 == 0) and (2 <= n <= 5 or n > 20):
        answer = "Not Weird"
    
    return answer

n = 3
result = weird_or_not(n)
print(result)
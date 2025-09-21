def vowel_counter(s):
    vowels = "AEIOU"

    for i in range(len(s)):
        if s[i] in vowels:
            print(s[i])

s = "BANENI"
result = vowel_counter(s)
print(result)
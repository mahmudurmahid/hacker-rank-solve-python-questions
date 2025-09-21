def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap

# alt solution - longer logic
def alt_is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            else: # year % 400 != 0
                leap = False
        else: # year % 100 != 0
            leap = True
    else: # year % 4 != 0
        leap = False

    return leap

year = 1990
result = is_leap(year)
print(result)
alt_result = alt_is_leap(year)
print(result)
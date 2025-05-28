def runnerup_score(arr):
    unique_scores = set(arr) # remove any duplicate scores in arr
    ascending_scores = sorted(unique_scores, reverse=True)

    second_highest_score = ascending_scores[1]

    return second_highest_score

arr = [2, 3, 6, 6, 5]
result = runnerup_score(arr)
print(result)
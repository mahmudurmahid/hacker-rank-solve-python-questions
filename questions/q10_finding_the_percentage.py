def finding_percentage(dictionary, queryname):
    # find all values (i.e. scores) from key (i.e. key=queryname)
    scores = dictionary.get(query_name)

    average = sum(scores) / len(scores)
    return average

students = {
    "Krishna": {67, 68, 69},
    "Arjun": {70, 98, 63},
    "Malika": {52, 56, 60}
}
query_name = "Malika"
result = finding_percentage(students, query_name)
print(result)
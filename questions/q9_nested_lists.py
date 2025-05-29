def student_grades(arr_list):
    # highest to lowest list of grades & unique scores from this list
    ascending_scores = sorted(arr_list, key=lambda x: x[1], reverse=True)
    unique_scores = sorted(set([score for name, score in ascending_scores]), reverse=True)

    # find the lowest grade and second lowest grade
    lowest_grade = ascending_scores[-1][-1]
    second_lowest_grade = unique_scores[-2]
    
    # find names of students with the second lowest grade
    second_lowest_grade_students = [name for name, score in ascending_scores if score == second_lowest_grade]

    names = []
    # sort the names alphabetically into names list
    for student in sorted(second_lowest_grade_students):
        names.append(student)

    return names


arr_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
result = student_grades(arr_list)
print(result)
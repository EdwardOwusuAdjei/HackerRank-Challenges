import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    values = [int(x) for x in grades]
    print(type(values[0]))
    lowest_point = 40 - 3
    grades_rounded = []

    for x in values:
        if x < lowest_point:
            grades_rounded.append(x)
        if x >= lowest_point:
            next_round = (int(x / 5) + 1) * 5
            difference = next_round - x
            if difference < 3:
                grades_rounded.append(next_round)
            else:
                grades_rounded.append(x)
    return grades_rounded




if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    #f.write('\n'.join(map(str, result)))
    #f.write('\n')

    #f.close()
#finding the highest score

'''You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x

Example Input : 78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output : The highest score in the class is: 91'''

def finding_highest_score(list):
    max_score=0
    for mark in list:
        if mark>=max_score:
            max_score=mark
        else:
            continue
    return max_score

print(finding_highest_score([78, 65, 89, 86, 55, 91, 64, 89]))
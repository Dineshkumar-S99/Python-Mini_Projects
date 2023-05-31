#finding the average of the height of given input and round the value

'''e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.'''

def finding_avg_height(*args):
    students = len(args)
    sum_of_heights=0
    for height in args:
        sum_of_heights+=height
    avg_height= sum_of_heights/students
    return round(avg_height)

print(finding_avg_height(180, 124, 165, 173, 189, 169, 146))

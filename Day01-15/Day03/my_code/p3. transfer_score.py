'''
score upper 90 --> A
score 80 ~ 89  --> B
score 70 ~ 79  --> C
score 60 ~ 69  --> D
score lower 60 --> E
'''

score = float(input("please enter your score: "))
if score > 100 or score < 0:
    grade = "ERROR. Enter the real score 0~100."
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print("The grade is: ", grade)
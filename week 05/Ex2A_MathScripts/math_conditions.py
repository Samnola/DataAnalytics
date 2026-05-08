# calculate letter grade for an exam score 

points_possible = 85

raw_score = int(input("Student score (raw points):"))

score = raw_score / points_possible

print(f'Raw percent score, unformatted: {score}')
print(f'percentage score is {score:.0%}')

if score >= .90:
    grade = 'A'
elif score >= .80:
    grade ='B'
elif score >= .70:
    grade = 'c'
elif score >= .60:
    grade = 'D'
else:
    grade = 'F'

print(f'student exam grade is {grade}')
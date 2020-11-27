# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

subject_count = 3
grade = ''

kor, eng, math = map(int, input().split())

total_score = kor + eng + math
avg = float(total_score / subject_count)

if avg >= 90:
	grade = 'A'
elif avg >= 80:
	grade = 'B'
elif avg >= 70:
	grade = 'C'
elif avg >= 60:
	grade = 'D'
else:
	grade = 'F'
	
print(format(avg, '.2f'), grade)

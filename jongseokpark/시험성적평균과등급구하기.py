# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math
user_input = input()
user_input = user_input.split(" ")

score = []
for i in user_input:
  score.append(int(i))

score_avg = (sum(score)/len(score))

def check_grade(score_avg):
  if score_avg >= 90:
    return "A"
  elif score_avg >= 80:
    return "B"
  elif score_avg >= 70:
    return "C"
  elif score_avg >= 60:
    return "D"
  else:
    return "F"
print("%(score_avg).2f %(grade)s" % {'score_avg': score_avg, "grade": check_grade(score_avg)})


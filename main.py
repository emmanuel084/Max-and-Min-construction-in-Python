# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maximo_score = 0
for maximo in student_scores:
  if maximo > maximo_score:
    maximo_score = maximo 

minimo_score = 0
for minimo in student_scores:
  if minimo < minimo_score:
    minimo_score = minimo

print(f"The highest score in the class is: {maximo}, but also your lowest score is: {minimo}") 
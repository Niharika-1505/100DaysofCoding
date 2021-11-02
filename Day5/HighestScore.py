# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
highest_score = 0
for i in student_scores:
    if i > highest_score:
        highest_score = i
print("Highest score generated using for loop:", highest_score)

print("Highest score generated using max method:", max(student_scores))
# Write your code below this row 👇

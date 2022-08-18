no_of_students, no_of_subjects = map(int, input().split())
score = []
for _ in range(no_of_subjects):
    score.append(list(map(float, input().split())))
for i in list(zip(*score)):
    print("%.1f" % (sum(i) / len(i)))
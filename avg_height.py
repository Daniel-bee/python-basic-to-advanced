student_heights = input("Input a list of student height ").split()
sum_ = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_ += int(student_heights[n])
print(student_heights)
avg = round(sum_/len(student_heights))
print(f"Avrage Height is: {avg}")

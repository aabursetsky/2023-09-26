grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

gradess = [sum(grades[0]) / len(grades[0]),
           sum(grades[1]) / len(grades[1]),
           sum(grades[2]) / len(grades[2]),
           sum(grades[3]) / len(grades[3]),
           sum(grades[4]) / len(grades[4])]

sorted_students = sorted(students)             # возвращает список

result = {gradess[0]:sorted_students[0],
          gradess[1]:sorted_students[1],
          gradess[2]:sorted_students[2],
          gradess[3]:sorted_students[3],
          gradess[4]:sorted_students[4]}
# result = dict(zip(sorted_students, gradess)) # как вариант
print(result)

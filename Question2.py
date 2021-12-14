#array of student grades
grades = [73,67,38,33]
#new array to store the rounded up grades of the students
new_grades = []

#looping through the grades of the students
for x in grades:
  val = x
  #looping and finding what number between 1 or 2 that will make the grade the next multiple of 5
  for i in range(3):
    if x >= 38 and (x+i) % 5 == 0:
      #adding that number to the grade to make it the next multiple of 5
      val = x + i
  #adding the new grades to the new array
  new_grades.append(val)

#printing out the old and new grades of the students
print(grades)
print(new_grades)

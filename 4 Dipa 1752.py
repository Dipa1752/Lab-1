# Initial array of student grades
grades = [85, 78, 92, 45, 33, 67, 88, 41]

# a. Use a for loop with if-else conditions to categorize each student's grade
print("Grade Categories:")
for score in grades:
    if score > 80:
        grade = 'A'
    elif 60 <= score <= 80:
        grade = 'B'
    elif 40 <= score < 60:
        grade = 'C'
    else:
        grade = 'F'
    print(f"Score: {score} - Grade: {grade}")

# b. Function to boost each student's grade by 5%
def boost_grades(grade):
    return grade * 1.05

# Use map() to apply boost_grades function to all grades
boosted_grades = list(map(boost_grades, grades))
print("\nBoosted Grades:")
print(boosted_grades)

# c. Use a lambda function to find boosted grades above 90
boosted_above_90 = list(filter(lambda x: x > 90, boosted_grades))
print("\nBoosted Grades Above 90:")
print(boosted_above_90)

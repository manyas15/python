# find if the student has passed or failed if it requires 40% to pass and the student has scored 33% in each subject to pass
# assume that the student has 3 subjects
# and take marks of each subject from the user

s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))

total_percentage = (100 * (s1 + s2 + s3) / 300)

if(total_percentage >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33):
    print("You have passed" , total_percentage)

else:
    print("You have failed" , total_percentage)


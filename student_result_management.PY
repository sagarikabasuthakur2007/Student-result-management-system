# Student Result Management System
print("STUDENT'S DETAILS")
student = input("Student Name : ")
studentroll = input("Student Rollno. : ")
print("STUDENT'S MARKS")
marks1 = int(input("Bengali : "))
if marks1 >= 40:
    print("Pass")
else:
    print("Fail")
marks2 = int(input("English : "))
if marks2 >= 40:
    print("Pass")
else:
    print("Fail")
marks3 = int(input("Math : "))
if marks3 >= 40:
    print("Pass")
else:
    print("Fail")
total = marks1+marks2+marks3
average = total/3
percentage = (total/300)*100
print("Total : ", total)
print("Average : ", average)
print("Percentage : ", percentage)
if marks1>=40 and marks2>=40 and marks3>=40:
    print("Overall Pass")
else:
    print("Overall Fail")
if percentage >= 90 and percentage <=100:
    print("Grade : A+")
elif percentage >= 80:
    print("Grade : A")
elif percentage >= 70:
    print("Grade : B+")
elif percentage >= 60: 
    print("Grade : B")
elif percentage >= 50: 
    print("Grade : C")
elif percentage >= 40: 
    print("Grade : D")
else:
    print("FAIL")
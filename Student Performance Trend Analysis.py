subjects = []
exam1 = []
exam2 = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("Enter subject name: ")
    m1 = int(input("Enter Exam 1 marks: "))
    m2 = int(input("Enter Exam 2 marks: "))

    subjects.append(name)
    exam1.append(m1)
    exam2.append(m2)

for i in range(n):
    difference = exam2[i] - exam1[i]

    print(subjects[i])

    if difference > 0:
        print("Improved")
    elif difference < 0:
        print("Declined")
    else:
        print("No Change")

    print("Difference:", difference)
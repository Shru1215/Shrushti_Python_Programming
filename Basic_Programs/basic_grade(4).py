# determine grade eligibility  based on subject marks (e.g, pass or fail per subject and overall) 

marks = 90

if  marks >= 90:
    print("grade: A+")
elif marks >= 80 :
    print("grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")
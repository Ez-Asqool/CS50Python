# score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
    
"""
    this code is correct, but we can
    tighting it up, reduce the propability of bugs, increase the readability of it 
    and we can increase the effechiancy of it by asking a fewer questions and get the same result.
    
"""

# score = int(input("Score: "))

# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

#more better:

score = int(input("Score: "))

if score >= 90 :
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

"""
    parity: even/odd checker program ---> go to parity.py 
"""
def say_hi():
    print("Hello Function")
    print("Hellow Working")

say_hi()
say_hi()
say_hi()


# FUnction Parameters, & FUnction Arguments

def calculate_percentage(obt_marks,total_marks):
    percentage=obt_marks/total_marks*100
    print(percentage)

calculate_percentage(858,1100)
calculate_percentage(950,1100)

# Make Function for Bmi Calculate

def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    if(bmi<=18.5):
        print("Underweight")
    elif (bmi>18.5 and bmi<=24.5):
        print("Normal")
    elif (bmi>24.5 and bmi<=29.9):
        print("Overweight")
    elif (bmi>30 and bmi<=39.9):
        print("Overweight")
    else:
        print("Severly Obese")

calculate_bmi(50,1.6764)


# Function Jisko Argment birthYear == 2026-birthYear ==, If 
# checkEligibility

def checkEligibility(birthYear):
    age=2026-birthYear
    if(age>=18):    
        print("Allow")
    else:
        print("DIsAllow")


checkEligibility(2010)
checkEligibility(2006)
checkEligibility(1994)
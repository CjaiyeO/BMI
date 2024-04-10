height=float(input("Enter your height in metres:- "))
weight=float(input("Enter your weight in kilograms:- "))
height2=height*height
bmi=weight/height2
print("Your BMI is ",bmi)
if(bmi>0):
    if(bmi<16):
        print("You are severely underweight")
    elif(bmi<17):
        print("You are moderately underweight")
    elif(bmi<18.5):
        print("You are underweight")
    elif(bmi<25):
        print("You are healthy")
    elif(bmi<30):
        print("You are  obese")
    elif(bmi<35):
        print("You are moderately obese")
    elif(bmi<=40):
        print("You are severly obese")
    elif(bmi>40):
        print("You are morbidly obese")
else:
    print("Incorrect information")



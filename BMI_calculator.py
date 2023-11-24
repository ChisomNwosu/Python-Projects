name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height= int(input("Enter your height in inches: "))
Bmi = (weight * 703) / (height * height)
print(Bmi)

if Bmi > 0:
    if (Bmi <= 18.5):
        print(name +", you are under weight")
    elif (Bmi <= 24.9):
        print(name + ", you are normal weight")
    elif (Bmi <= 29.9):
        print(name + ", you are overweight, you need to exercise more and stop playing games")
    elif (Bmi <= 34.9):
        print(name + ", you are obese")
    elif (Bmi <= 39.9):
        print(name +", you are severly obese ")
    else:
        print(name + ", you are mobidly obese")      
else:
    print("Enter valid input")

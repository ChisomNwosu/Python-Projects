name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height= int(input("Enter your height in inches: "))
BMI = (weight * 703) / (height * height)
print(BMI)

if BMI > 0:
    if (BMI <= 18.5):
        print(name +", you are under weight")
    elif (BMI <= 24.9):
        print(name + ", you are normal weight")
    elif (BMI <= 29.9):
        print(name + ", you are overweight, you need to exercise more and stop playing games")
    elif (BMI <= 34.9):
        print(name + ", you are obese")
    elif (BMI <= 39.9):
        print(name +", you are severly obese ")
    else:
        print(name + ", you are mobidly obese")      
else:
    print("Enter valid input")

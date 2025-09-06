# BMI Category

height=float(input("Enter height in meters: "))
weight=float(input("Enter weight in kilograms: "))

BMI=weight/(height**2)

if(BMI>=30):
    print("\"Obesity\"")

elif(BMI>25 and BMI<=29):
    print("\"Overweight\"")

elif(BMI>18.5 and BMI<=25):
    print("\"Normal\"")

elif(BMI<=18.5):
    print("\"Underweight\"")

else:
    print("There is something wrong!")
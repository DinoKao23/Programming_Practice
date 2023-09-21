pounds = float(input("Enter the weight in pounds: "))
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

Calculation = (pounds*0.45359237)/(((feet*12+inches)*0.0254)**2)

print(f"BMI is {round(Calculation,2)}")

if Calculation < 18.5:
    print("Underweight")
elif Calculation < 25:
    print("Normal")
elif Calculation < 30:
    print("Overweight")
else:
    print("Obese")
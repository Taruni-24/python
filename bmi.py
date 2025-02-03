weight=int(input("enter weight in kgs: "))
height=float(input("enter height in metres: "))
bmi=weight/height**2
print(round(bmi))
if (bmi<18.5):
    print(f"Your BMI is {bmi} and you are underweight.")
elif (bmi<25):
    print(f"Your BMI is {bmi} and you are normalrweight.")
else:
    print(f"Your BMI is {bmi} and you are overweight.")
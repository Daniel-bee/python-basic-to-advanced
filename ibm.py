height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
ibm = int(weight / height ** 2)
status = ""
if ibm < 18.5:
    status = "Underweight"
elif ibm > 18.5 and ibm < 25:
    status = "Normal Weight"
elif ibm > 25 and ibm < 30:
    status = "Over Weight"
elif ibm > 30 and ibm < 35:
    status = "Obese"
elif ibm > 35:
    status = "Clinically obese"
print(f"Your BMI is {ibm}, you are slightly {status}")

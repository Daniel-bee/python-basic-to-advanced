age = input("What is your current age? ")
age_left = 90 - int(age)
weeks = age_left * 52
days = age_left * 365
months = age_left * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left")
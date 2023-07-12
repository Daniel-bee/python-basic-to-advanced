from random import randint
names = input("Give me everybody's name separated by comma. ")

split_name = names.split(", ")
idx = randint(0, len(split_name) -1)
print(f"{split_name[idx]} is going to buy the meal today")

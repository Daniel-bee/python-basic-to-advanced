print("Welcome to the Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_name = (name1 + name2).lower()

count_true = 0
count_true += combined_name.count("t") 
count_true += combined_name.count("r")
count_true += combined_name.count("u")
count_true += combined_name.count("e")
count_love = 0
count_love += combined_name.count("l")
count_love += combined_name.count("o") 
count_love += combined_name.count("v")
count_love += combined_name.count("e")

love_score = int(str(count_true) + str(count_love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} you are alright together")
else:
    print(f"Your score is {love_score}")
    
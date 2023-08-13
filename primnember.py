def prime_checker(number):
    flag = 1
    for i in range(2, number):
        if number % i == 0:
            flag = 0
            break
    if flag:
        print("It's prime number")  
    else:
        print("It's not prime number")  

n = int(input("Check this number "))

prime_checker(number=n)
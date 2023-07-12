even_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num
print(f"The even sum from 1 to 100 is: {even_sum}")

total = 0
for num in range(1, 100, 2):
    total += num
    
print(f"[Using range step method] The even sum from 1 to 100 is: {total}")
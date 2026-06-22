n = int(input("Enter a number: "))

divisors = [2, 3, 5, 7, 11]

for d in divisors:
    if n % d == 0:
        print(f"It is divisible by {d}")
n = int(input("Enter a number: "))

divisors = [2, 3, 5, 7, 11]

# Variation 1
for d in divisors:
    if n % d == 0:
        print(f"It is divisible by {d}")

# Variation 2
for i in range(1,12):
    if n%i == 0:
        print(f"It is divisible by {i}")
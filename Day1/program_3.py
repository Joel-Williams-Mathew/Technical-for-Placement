n = int(input("Enter the number :"))

for i in range(n):
    row = []
    for j in range(n - 1 - i):
        row.append("_")
    for j in range(i + 1):
        row.append("*")
    print(" ".join(row))

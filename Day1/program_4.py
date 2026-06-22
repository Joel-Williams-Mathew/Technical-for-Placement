" _ _ * "
" _ * * * "
" * * * * * "               # for n=3
" _ * * * "
" _ _ * "

n = int(input("Enter the number :"))

# Top half (including middle row)
for i in range(n):
    row = []
    for j in range(n - 1 - i):
        row.append("_")
    for j in range(2 * i + 1):
        row.append("*")
    print(" ".join(row))
                                                                                # 2 * n - 1 will have 5 stars which will be the biggest row length with stars for n=3
# Bottom half (mirror, without repeating middle row)                         
for i in range(n - 2, -1, -1):
    row = []
    for j in range(n - 1 - i):
        row.append("_")
    for j in range(2 * i + 1):
        row.append("*")
    print(" ".join(row))

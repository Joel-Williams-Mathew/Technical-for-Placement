" 1 3 5 7 9 "
" 3 5 7 9 1 "
" 5 7 9 1 3 "                        # for n = 5
" 7 9 1 3 5 "
" 9 1 3 5 7 "


" 1 3 5 7  "
" 3 5 7 1 "
" 5 7 1 3 "                        # for n = 4
" 7 1 3 5 "



n = int(input("Enter n: "))

nums = []

# Generate first n odd numbers
for i in range(n):
    nums.append(2 * i + 1)

# Print pattern
for i in range(n):
    for j in range(n):
        print(nums[(i + j) % n], end=" ")
    print()
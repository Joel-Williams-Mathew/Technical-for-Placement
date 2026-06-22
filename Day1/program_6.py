'''
4 4 4 4 4 4 4
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''

n = int(input("Enter n: "))

size = 2 * n - 1

for i in range(size):        #row
    for j in range(size):    #column

        top = i
        left = j
        bottom = size - 1 - i
        right = size - 1 - j

        distance = min(top, left, bottom, right)

        print(n - distance, end=" ")

    print()


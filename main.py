
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


print("sum of rows: ",end = "")

TOTAL = sum(numbers[0])
INDEX = 0

for i in range(len(numbers)):
    print(sum(numbers[i]))
    if(TOTAL<sum)(numbers[i]):
        TOTAL = sum(numbers[i])
        INDEX = i

print("\nSum of columns: ", end = " ")
GREATEST = numbers[0][0]
for j in range(len(numbers[0])):
    TOTAL = 0
    for i in range(len(numbers[0])):
        TOTAL += numbers [i][j]
        if GREATEST<numbers[i][j]:
            GREATEST = numbers[i][j]
    print(TOTAL,end= " ")
print(f"\nRow with greatest sum:{INDEX}")
print(f"the greatest number: {GREATEST}")

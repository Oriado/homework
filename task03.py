rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of colums: "))

matrix = []

print("Enter the elements row by row: ")

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Element [{i+1},{j+1}]: "))
        row.append(value)
    matrix.append(row)

print("\nOriginal matrix: ")
for r in matrix:
    print(r)
    
transposed = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print("\nTransposed matrix: ")
for r in transposed:
    print(r)                
        
        
row = int(input("enter no of rows: " ))
col = int(input("enter no of cols:"))
print("enter MATRIX :  ")
matrix=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()

for i in range(row):
    for j in range(col):
        if i==j and matrix[i][j]==1:
            success=1
        elif matrix[i][j]!=0:
            print("not a unit matrix")
            exit()
if success==1:
    print("it is a unit matrix")

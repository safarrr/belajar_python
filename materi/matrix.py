# mat1 = [[1,2,3],[1,1,3],[0,5,4]]
# mat2 = [[3,3,2],[2,4,7],[1,2,5]]
# for x in range(0, len(mat1)):
#     for y in range(0, len(mat1[x])):
#         print(mat1[x][y] + mat1[x][y], end=" " )
mat1 = [[4,5],[2,6]]
mat2 = [[1,2],[3,4]] 
mat3 = []
for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0 
        for z in range(0,len(mat1)):
            total  = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
        print(row)
    mat3.append(row)

for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):  
        print(mat3[x][y], end=" ")
    print(" ")
 
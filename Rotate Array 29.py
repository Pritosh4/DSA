'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

Input Format

The first line have the M value
Second line have N value
Third-line onwards, the next 'N' lines or rows represent the ith row values.
Each of the ith rows constitutes column values separated by a single space
Constraints

No

Output Format

90 degree Rotated Matrix in single line.
Sample Input 0

3
3
1 2 3
4 5 6
7 8 9
Sample Output 0

7 4 1 8 5 2 9 6 3
Sample Input 1

3
3
1 12 3
4 15 6
7 18 9
Sample Output 1

7 4 1 18 15 12 9 6 3'''

def rotate(matrix, R, C):
    for i in range(R):
        for j in range(i,C):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    for i in range(R):
        for j in range(C//2):
            matrix[i][j], matrix[i][C-j-1] = matrix[i][C-j-1], matrix[i][j]
    return matrix

R = int(input())
C = int(input())
matrix =[]
for i in range(R):
    matrix.append(list(map(int, input().split())))
    
for i in rotate(matrix, R, C):
    for j in i:
        print(j, end = ' ')
    

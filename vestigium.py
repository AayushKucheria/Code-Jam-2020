# PROBLEM
# Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.
# The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper
# left to the lower right).
#
# An N-by-N square matrix is a Latin square if each cell contains one of N different values,
# and no value is repeated within a row or a column.
# In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1
# and N.
# Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is
# a natural Latin square. To give some additional information, instead of simply telling us whether the matrix is
# a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated
# values.
#
# INPUT
# The first line of the input gives the number of test cases, T. T test cases follow.
# Each starts with a line containing a single integer N: the size of the matrix to explore.
# Then, N lines follow. The i-th of these lines contains N integers Mi,1, Mi,2 ..., Mi,N. Mi,j is the integer
# in the i-th row and j-th column of the matrix.
#
# OUTPUT
# For each test case, output one line containing Case #x: k r c, where x is the test case number
# (starting from 1), k is the trace of the matrix, r is the number of rows of the matrix that contain repeated
# elements, and c is the number of columns of the matrix that contain repeated elements.


# SOLUTION
# Calculating the trace by adding diagonals, and using the property of sets that it can only hold
# unique elements to our advantage to calculate the number or rows/columns that have repeat elements.

test_cases = int(input())
allCase = []  # Storing Case Number
allTrace = []  # Storing traces for each case
allCountRow = []  # Storing count of rows that contain repeated elements for each case
allCountCol = []  # Same for columns

for i in range(test_cases):
    size = int(input())
    matrix = []

    # Inputting Rows
    for j in range(size):
        row = map(int, input().split(" "))
        matrix.append(list(row))

    # Compute Trace by adding the diagonals
    trace = 0
    for loc in range(size):
        diagonals = matrix[loc][loc]
        trace = trace + diagonals

    seen = set()
    countRow = 0
    countCol = 0

    # Since sets only contain unique elements, we can use this property to see if
    # a row/column has repeat elements or not
    for row in range(size):
        if len(matrix[row]) != len(set(matrix[row])):
            countRow += 1

        colList = []
        for col in range(size):
            colList.append(matrix[col][row])

        if len(colList) != len(set(colList)):
            countCol += 1

    allCase.append(str(i + 1))
    allTrace.append(str(trace))
    allCountRow.append(str(countRow))
    allCountCol.append(str(countCol))
    # print("Case #"+ str(i+1) + ": " + str(trace) + " " + str(countRow) + " " + str(countCol))

# Computation Done. Final Output
for i in range(len(allCase)):
    print("Case #" + allCase[i] + ": " + allTrace[i] + " " + allCountRow[i] + " " + allCountCol[i])

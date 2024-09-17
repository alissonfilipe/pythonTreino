import numpy as np  # Import NumPy library

# Read the size of the matrix (n x n)
n = int(input())

# Initialize a list to store the rows of the matrix
matrix = []


for _ in range(n):
    # Read a row of the matrix, split by spaces, and convert to float
    row = list(map(float, input().split()))
    
    # Check if the number of elements in the row is equal to n
    if len(row) != n:
        print(f"Error: Each row must contain exactly {n} elements.")
        break
    
    # Add the row to the matrix
    matrix.append(row)

# Convert the list of lists into a NumPy array
matrix = np.array(matrix)

# Check if the matrix is square before calculating the determinant
if matrix.shape[0] == matrix.shape[1]:
    # Calculate the determinant using numpy.linalg.det
    determinant = np.linalg.det(matrix)
    # Print the determinant rounded to 2 decimal places
    print(f"{round(determinant, 2)}")
else:
    print("Error: The matrix is not square.")

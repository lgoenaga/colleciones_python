from grid import Grid


matrix = Grid(3, 3)

for row in range(matrix.get_height()):
  for col in range(matrix.get_width()):
    matrix[row][col] = row + col
    
print(matrix)
print(matrix.__getitem__(1)[0])
# Minesweeper Game

# We need a list with the location of the bombs [x,y], the number of rows and
# colummns of the game.

# Creating a function:
def mine_sweeper(bombs, num_rows, num_cols):

  # Creating the mine field
  field = [[0 for i in range(num_cols)] for j in range(num_rows)]

  # Alocating the bombs on field
  for bomb_location in bombs:
    (bomb_row, bomb_col) = bomb_location
    field[bomb_row][bomb_col] = -1  # The bombs will be represented by -1

  # Creating an imaginary matrix to analyse the nearby bombs
    row_range = range(bomb_row - 1, bomb_row + 2)
    col_range = range(bomb_col - 1, bomb_col + 2)

  # Filling the cells with the number of the nearby bombs
    for i in row_range:
      for j in col_range:
        if (0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
          field[i][j] += 1

  return field

print(mine_sweeper([[0,0], [1,2]], 3, 4))

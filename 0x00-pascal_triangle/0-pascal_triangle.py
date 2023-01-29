#!/usr/bin/python3
def pascal_triangle(n):
  """draws a pascal triangle
  Args:
      n (n): size of triangle
  Returns:
      list: returns empty list if n <= 0 or list of lists of integers
      representing Pascal's triangle of n otherwise
      parameters:
      n[init]
  """
  
  if type(n) is not int:
    raise TypeError("n must be an integer")

  pascal_triangle = []
  if n <= 0:
    raise ValueError("n must be greater than 0")

  previous = []
  for i in range(n):
    temp_list = []
    for j in range(i + 1):
      if j == 0 or j== i:
        temp_list.append(1)

      else:
        temp_list.append(previous[i - 1][j - 1] + previous[i - 1][j]) 

    previous.append(temp_list)


  for i in range(n):
    for j in range(n - i - 1):
      print(format(" ", "<2"), end=" ")

    for j in range(i + 1):
      print(format(previous[i][j], "<4"), end=" ")

    print()


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
    return pascal_triangle

  previous = [1]

  for row_i in range(n):
    rowlist = []
    if row_i == 0:
      rowlist = [1]

    else:
      for i in range(row_i + 1):
        if i == 0:
          rowlist.append(0 + previous[i])
        elif i == (row_i):
          rowlist.append(previous[i -1] + 0)

        else:
          row_i.append(previous[i - 1] + previous[i])

    previous = rowlist
    pascal_triangle.append(rowlist)

  return pascal_triangle
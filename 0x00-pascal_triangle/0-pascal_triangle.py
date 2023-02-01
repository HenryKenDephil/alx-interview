#!/usr/bin/python3
"""
Pascal's Triangle
"""
def pascal_triangle(n):
  """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n or an empty list if n <= 0
  """
  
  triangle = list()
  triangle.append([1])
  for i in range(n - 1):
    temp_list = [0] + triangle[-1] + [0]
    row = list()
    for j in range(len(triangle[-1]) + 1):
      row.append(temp_list[j] + temp_list[j + 1])

    triangle.append(row)
  return triangle

'''
if __name__=='__main__':
  tr = pascal_triangle()
  for lst in tr:
    print (lst)
'''
#!/usr/bin/python3
#python program that draws a pascal triangle
#the program will return a list of integers representing pascal triangle of size n
def pascal_triangle(n):
  '''a function to that draws a psacal triangle
      Returns:
            a list of integers representing pascal triangle of n
            an empty list if n <= 0
      Assumes that n is always an integer 
      Args:
            n (n): size of triangle
  '''
  
  triangle = list()
  triangle.append([1])
  for i in range(n - 1):
    temp_list = [0] + triangle[-1] + [0]
    row = list()
    for j in range(len(triangle[-1]) + 1):
      row.append(temp_list[j] + temp_list[j + 1])

    triangle.append(row)
  return triangle

if __name__=='__main__':
  tr = pascal_triangle(6)
  for lst in tr:
    print (lst)
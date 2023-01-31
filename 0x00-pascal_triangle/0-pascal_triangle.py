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
  
  #check if n is an integer
  if type(n) is not int:
    raise TypeError("n must be an integer")

  #check if n is greater than zero
  if n <= 0:
    raise ValueError("n must be greater than 0")

 #set the current list
  previous = []

 #generate the pattern list
  for i in range(n):
    temp_list = []
    for j in range(i + 1):
      if j == 0 or j== i:
        temp_list.append(1)

      else:
        temp_list.append(previous[i - 1][j - 1] + previous[i - 1][j]) 

    previous.append(temp_list)

#print the pascal triangle pattern
  for i in range(n):
    for j in range(n - i - 1):
      print(format(" ", "<2"), end=" ")

    for j in range(i + 1):
      print(format(previous[i][j], "<4"), end=" ")

    print()


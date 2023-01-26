#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(" ", end=" ")
            
        #assign first element e to be 1
        e = 1
        for j in range(1, i+1):

            #always expect the first value in the line to be 1
            
            print(" ", e, sep=" ", end=" ")

            #apply the concept of Bionomial Coefficients

            e = e *(i-j)//j
        print()



pascal_triangle(n)

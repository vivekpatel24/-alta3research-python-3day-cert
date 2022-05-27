#!/usr/bin/env python3

"""Vivek Patel | Learning Python 
   Creating a simple three number addition program."""

def main():
    
    #Input a number
    set1 = input("Enter the first number: ")
    set2 = input("Enter the second number: ")
    set3 = input("Enter the third number: ")
					
    # Adding number together
    sum = float(set1) + float(set2) + float(set3)
								
    #Display the aggregate 
    print ("The sum of {0} and {1} and {2} is {3}".format(set1, set2, set3, sum))
												
main()
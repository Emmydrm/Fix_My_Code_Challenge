#!/usr/bin/python3
""" FizzBuzz
"""
# There seems to be an error in your implementation of the FizzBuzz function. 
# Specifically, in the second elif statement, you're checking for multiples of 3 instead of multiples of both 3 and 5. 
# Here's the corrected version of the fizzbuzz function:
import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For multiples of three print "Fizz" instead of the number and for
    multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
        print(" ".join(tmp_result))


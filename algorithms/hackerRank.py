#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
#
def gradingStudents(grades):
    gd = []
    for i in range(len(grades)):
        mul = 1
        while grades[i] > 5*mul:
            mul +=1
        if grades[i] < 38:
            gd.append(grades[i])
        elif abs(grades[i] - mul*5) <3:
            g = mul*5
            gd.append(g)
        elif abs(grades[i] -mul*5) >=3:
            gd.append(grades[i])

    return gd



if __name__ == '__main__':
    grades = [75, 74, 67, 33]
    result = gradingStudents(grades)
    print result

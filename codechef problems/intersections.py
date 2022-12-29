# Intersections

# Problem Statement
# You are given N points in the plane. The points are numbered from 1 to N. For each pair of points, you need to find the number of other points that lie between them. Two points are said to lie between a pair of points if they lie on the line segment joining the two points.

# Input
# The first line contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer N.
# N lines follow. For each valid i, the i-th of these lines contains two space-separated integers xi and yi denoting the coordinates of the i-th point.
# Output
# For each test case, print N lines. For each valid i, the i-th of these lines should contain N−1−cnti integers, where cnti is the number of points that lie between the i-th point and the other points. The integers should be space-separated and should be sorted in non-decreasing order.

# Constraints
# 1≤T≤10
# 3≤N≤105
# −109≤xi,yi≤109
# the sum of N over all test cases does not exceed 105
# Subtasks
# Subtask #1 (100 points): original constraints

# Example Input
# 1
# 4
# 0 0
# 1 0
# 0 1
# 1 1
# Example Output
# 0 1 1 2
# 1 0 2 1
# 1 2 0 1
# 2 1 1 0
# Explanation
# Example case 1: The first point lies between the second and third point. The second point lies between the first and fourth point. The third point lies between the first and fourth point. The fourth point lies between the second and third point.

# Solution
# Python3 program to find the number of points
# lying between two points in a plane.

from collections import Counter, defaultdict, deque
from typing import List

# Function to find the number of points
# lying between two points in a plane.
def lineintersection(n):  # plan cordinate 
    number_of_lines = 0
    


    
                
# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(lineintersection(n))

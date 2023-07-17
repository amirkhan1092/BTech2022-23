'''This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].'''


def string_occurance(string, pattern):
    indics = []
    for i in range(len(string)):
        if string[i:i+len(pattern)] == pattern:
            indics.append(i)
    return indics


print(string_occurance("rcdrcdr", "cdr"))



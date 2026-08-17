#problem 1
# Print the first 5 characters of a string.
"""P1 ="PythonProgramming"
print(P1[0:5])"""
#output: Pytho

# Problem 2
#Print the last 4 characters of a string.
"""print(P1[13:17])"""
#output: "ming"

#Problem 3
#Print every second character.
"""print(P1[::2])"""
#output: "PtoPormig"

#Problem 4: Reverse a string using slicing.
"""P1 = "Python"
print(P1[::-1])"""
# output: "nohtyP"

#Intermediate Problems
#Problem 1: Print string except first and last character
"""I = "Programming"
print(I[1:10]) #print(I[1:-1])"""

#Problem 2: Print first half of a string.
C = "Computer"
"""print(C[:4])"""
# output: "Comp"

#Problem 3: Print second half of the string.
"""print(C[4:])"""
#output: "uter"

#Problem 4: Print every third character.
"""E = "abcdefghijklmnopqrstyvwxyz"
print(E[::3])"""
#Output: "adgjmpsvy"

#Problem 5: Reverse only first 5 characters.
"""R = "PythonProgramming"
print(R[:5][::-1]+R[5:])"""

#Challenge Problems.
#Problem 11: Swap the first and last 3 characters of a string.
"""Input = "Programming"
print(Input[-3:]+Input[3:8]+Input[:3])"""

"""#Problem 13: Print string in reverse, skipping every alternate character.
PS = "PythonProgramming"
print(PS[::2][::-1])

#Problem 14: Remove first 2 and last 2 characters.
print(PS[2:15])"""

"""#Problem 15 : Print 01234, 56789, 02468, 97531
Given = "0123456789"
print(Given[0:5])
print(Given[5:10])
print(Given[::2])
print(Given[::-1])
print(Given[::-2])"""

#Probelm 12: Extract the middle 3 characters
Given = "Computer"
print(Given[3:6])
mid = len(Given)//2
print(Given[mid-2:mid+1])
#output: put


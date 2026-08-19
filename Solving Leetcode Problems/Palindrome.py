# Palindrome: Given an integer x, return true if x is a palindrome, and false otherwise. (leetcode)


a = int(input())
def isPalindrome(x):
    s = str(x)
    return s == s[::-1]
print(f"isPalindrome: {isPalindrome(a)}")
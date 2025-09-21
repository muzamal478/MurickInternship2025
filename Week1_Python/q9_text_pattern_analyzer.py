# Text Pattern Analyzer
# Checks for anagrams and longest common subsequence
from collections import Counter

def are_anagrams(s1, s2):
    return Counter(c.lower() for c in s1 if c.isalnum()) == Counter(c.lower() for c in s2 if c.isalnum())

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# Get input and run analysis
try:
    s1, s2 = input("Enter two strings (separated by space): ").split()
    print(f"Anagrams: {are_anagrams(s1, s2)}")
    print(f"Longest Common Subsequence Length: {lcs(s1, s2)}")
except ValueError:
    print("Error: Please enter two strings separated by a space.")
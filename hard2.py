def shortest_palindrome(s):
    def compute_kmp_table(pattern):
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = table[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            table[i] = j
        return table

    combined = s + '#' + s[::-1]
    kmp_table = compute_kmp_table(combined)

    # Find the length of the longest palindrome prefix
    palindrome_length = kmp_table[-1]

    # Return the shortest palindrome by adding the reverse of the remaining characters
    return s[palindrome_length:][::-1] + s
s = "abcd"
result = shortest_palindrome(s)
print(result)
'''
1.Combine the String with its Reverse
2.Compute the KMP Prefix Table
3.Find the Length of Longest Palindrome Prefix
4.Construct the Shortest Palindrome'''
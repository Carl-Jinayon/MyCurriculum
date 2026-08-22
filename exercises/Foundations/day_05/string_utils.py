def reverse_string(s):
    rev = ""
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    return rev

def count_vowels(s):
    count = 0

    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            count += 1
            
    return count

def is_palindrome(s):
    return s == reverse_string(s)

print(reverse_string("test"))
print(count_vowels("fsdafsddsdadaou"))
print(is_palindrome("haha"))
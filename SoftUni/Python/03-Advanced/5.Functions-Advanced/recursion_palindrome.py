def palindrome(word, index=0, result=""):
    if index == len(word):
        if word == result:
            return f"{word} is a palindrome"
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1, result + word[len(word) - 1 - index])


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
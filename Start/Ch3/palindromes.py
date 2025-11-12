def is_palindrome(teststr):
    # Your code goes here.
    teststr = teststr.lower()
    newstr =""
    for ch in teststr:
        if ch.isalnum():
            newstr += ch

    return newstr == newstr[::-1]

# test_word = "Madam, I'm Adam."
# try using some of these other words:
# test_word = "RACE CAR!"
test_word = "Hello, world"
# test_word = "Radar?"
# test_word = "A man, a plan, a canal Panama!"

print(is_palindrome(test_word))
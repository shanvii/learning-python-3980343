def find_largest(the_strings):
    # Your code goes here
    # res = 0
    # for s in the_strings:
    #     if len(s) > res:
    #         res = len(s)

    # return res
    return max(len(s) for s in the_strings)

test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]
print(find_largest(test_strings))
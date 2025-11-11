def count_numbers(which, numbers):
    # Your code goes here
    if which != "even" and which != "odd":
        return -1
    
    count = 0
    for n in numbers:
        if which == "even" and n % 2 == 0:
            count += 1
        if which == "odd" and n % 2 != 0:
            count += 1
    return count

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

print(count_numbers("even", numbers))
print(count_numbers("odd", numbers))
print(count_numbers("Blarg", numbers))
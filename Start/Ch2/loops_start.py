# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
while x < 5:
  print(x)
  x += 1

# answer = input("should loop stop?" )
# while answer != "yes":
#   print(answer)
#   answer = input("stop? ")

# define a for loop
nums = [1, 2, 3, 4, 5]
print("\n", nums)
for num in nums:
  if num == 2:
    continue
  if num == 4:
    break
  print(num)

# use a for loop over a collection


# use the break and continue statements


# using the enumerate() function to get an index and an item
print("using the enumerate() function to get an index and an item")
for i,n in enumerate(nums):
  print(i, n)
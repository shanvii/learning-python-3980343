# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements

x, y = 10, 100

# conditional flow uses if, elif, else
if x > y:
  print("x greater than y")
elif x == y:
  print("x and y equal")
else:
  print("y greater")

# conditional statements let you use "a if C else b"
result = "x > y" if(x > y) else "x = y or x < y"
print(result)
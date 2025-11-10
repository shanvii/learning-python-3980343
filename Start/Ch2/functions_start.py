# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def hello_func():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

hello_func()

# function that takes parameters
def para_func(greet):
  name = input("your name please? ")
  print(greet, name)

para_func("Hello ")

# function that returns a value
def retu_func(n):
  return n*n*n
print(retu_func(3))

# function with default value for an parameter
def def_func(greet, name = None):
  if name == None:
    name = input("name please: ")
  print(greet, name)

# def_func("hello", "shanvi")
# def_func("hello")
def_func(name="shanvi", greet="bye")

# function with variable number of parameters
def var_func(*args):
  res = 0
  for x in args:
    res += x
  print(res)

var_func(1, 2, 3, 4)
var_func(1, 2, 3, 4, 5)

# variable function mentioned last
def var_func(start, *args):
  res = 0
  for x in args:
    res += x
  print(res)

var_func(10, 1, 2, 3, 4)
# Functions and variaables
# 01. Input, variables, output

# name = input("What's your name? ")

# print("hello", name)


# 02. Strings and f-strings

# name = input("What's your name> ").strip().title()

# print("hello, " + name)
# print("hello, ", name)
# print(f"hello, {name}")

# first, last = name.split(" ")
# print(f"hello, {first}")

# Writing your own functions

# def main():
#     name = input("What's your name? ")
#     hello(name)
#     hello()

# def hello(to="world"):
#           print(f"hello, {to}")

# main()

# Return versus print
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n*n
main()
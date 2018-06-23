# Write a Python program to read last n lines of a file
with open("C:/Users/vijay/Documents/hello-git/Assignment_14/test.txt") as f:
    last = f.readlines()
# Taking input of last lines to be read from the file.
n = int(input("Enter the number of lines to be read: "))
print("The Last lines are: ", last[-n])
n -= 1
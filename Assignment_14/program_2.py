# Write a Python program to count the frequency of words in a file.
from collections import Counter  # Using counter inorder to count the frequency of words in the giver stored string

def word_count(fname):

        with open(fname) as f:
                return Counter(f.read().split())

# Using collections a and counter. Calling the function word_count & giving a path.
print("Number of words in the file :", word_count("C:/Users/vijay/Documents/hello-git/Assignment_14/test.txt"))
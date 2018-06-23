# Split the following irregular sentence into words
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"

Removed_stuff = ".,;_"      # all characters to be removed which has this in it.

sentence = """A, very very; irregular_sentence"""
for i in Removed_stuff:
    sentence = sentence.replace(i, ' ')

sentence.split()
print("Desired_Ouput: ", sentence)
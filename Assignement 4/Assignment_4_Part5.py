word ="MISSISSIPPI"
word_list = list(word)
print(word_list)
word_set = set(word_list)
print(word_set)
word_dict = {}
for x in word_set:
	word_dict[x] = word_list.count(x)

print(word_dict)
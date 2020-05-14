def sort_by_alphabet(string):
	string.sort()
	return string

list_of_letters = ['f', 'd', 'q', 'a', 'b', 'w', 'g', 'y', 't', 'p']

sort_by_alphabet(list_of_letters)

for i in list_of_letters:
	print(i, end=' ')

print()
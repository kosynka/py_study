# lambda func example
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')

# equivalence
def full_name2(first, last):
	print('Full name: {} {}'.format(first.title(), last.title()))

full_name2('sayat', 'kaldarbekov')

name = 'sayat'
print('{:.<10}'.format(name.title()))

(lambda x, y: x + y)(2, 3)
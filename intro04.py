def get_formatted_birthday(day, month, year):
    format_of_date = '%02d-%02d-%d' % (day, month, year)
    return format_of_date

def cortege_test(num, in_text=None):
	text = '''
	написать 4 нуля и заполнять слева: %04d;
	ввод строки: %s
	''' % (num, in_text)
	return text
	# переменная text - кортеж

print(cortege_test(23, 'Sayat'))
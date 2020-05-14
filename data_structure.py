# Стек или очередь LIFO

# Хэш-таблицы
book = dict()
book['1984'] = 1490
book['луна и грош'] = 2290
book['маленький принц'] = 1590

value = book.get('скотный двор')    # возвращает значение если книга есть, в противном случае None

search_for = input()
print('Price of book "{}" is {}'.format(search_for, book[search_for]))
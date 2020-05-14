def my_substr(string, index):
    sub_string = ''
    i = 0
    while i < index:
        current_char = string[i]
        sub_string += current_char
        i += 1
    return sub_string

print(my_substr('cvbnmlkjhv', 5))
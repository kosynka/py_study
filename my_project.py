def start():
    right_arrow = '>'
    left_arrow = '<'
    begin_text = 'Begin of project'
    print('{} {: ^4} {}'.format(left_arrow*32, begin_text, right_arrow*32))
    print('Please write here your name: ', end='')
    name = input()
    return name

def stop():
	print('Project was stopped')

user_name = start()

stop()
# import this # дзен питона

def my_try_except_test(n):
    print('*' * n)
    err1 = ''
    print('{} / 0 = {}'.format(n, 'error'))

    try:
        n = n / 0
    except Exception as e:
        err1 = '{}'.format(e.__class__)
        print(e.__class__, end=' - is error type. ')
        print('Exception is executed')
    else:
        print('Else is executed')
    finally:
        print('Code execution of Finally + {}'.format(err1))

my_try_except_test(66)
def func1(*args, **kwargs):
    print(args)
    for items in args:
        print(items)
    print("key words",kwargs)
    print(kwargs['lol'])

func1(1, 'abc', lol='lmao',lolwa='rlf')
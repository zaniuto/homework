def full_function(a, b, c=2, *args, **kwargs):
    return '\n'.join([
        f'parametr a ma wartość: {a}',
        f'parametr b ma wartość: {b}',
        f'parametr c ma wartość: {c}',
        f'inne argumenty pozycyjne: {args}',
        f'inne argumenty nazwane: {kwargs}'
    ])

call_kwargs = {
    'a': 1,
    'b': 2,
    'extra': 'ab',
}

full_function(1, 2)
full_function(1,2,None,True)
full_function(1,2, d=5)
full_function(1,2, 1, {'a':3})
full_function(1,d=4,b='xtra')
full_function(*[1,2,3,4])
full_function(**call_kwargs)
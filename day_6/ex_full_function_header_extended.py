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

options = dict(
    full_default=(
        'Wszystko domyślnie',
        full_function(1, 2),
    ),
    positional=(
        'Argumenty podane pozycyjnie',
        full_function(1,2,None,True),
    ),
    additional_kwarg=(
        'Dodatkowy nazwany parametr',
        full_function(1,2, d=5),
    ),
    postional_dict=(
        'Słownik podany jako parametr pozycyjny',
        full_function(1,2, 1, {'a':3}),
    ),
    named_call=(
        'Jawne wywołanie parametru pozycyjnego',
        full_function(1,d=4,b='xtra'),
    ),
    call_with_tuple=(
        'Wywołanie rozpakowaniem sekwencji',
        full_function(*[1,2,3,4]),
    ),
    call_with_dict=(
        'Wywołanie słownikiem',
        full_function(**call_kwargs),
    ),
    
)

print('{}:\n{}'.format(*options['call_with_dict']))
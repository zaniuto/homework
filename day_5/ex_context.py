a = 1
print('-'*15)
print('Globalnie')
print('scope: ', dir())
print('locals: ', locals().keys())
print('globals: ', globals().keys())

def local_ns():
    print('-'*15)
    print('Lokalnie (local_ns)')
    a = 2
    print('scope: ', dir())
    print('locals: ', locals().keys())
    print('globals: ', globals().keys())
    print('a', a)

local_ns()

def local_local_ns():
    print('-'*15)
    print('Lokalnie (local_local_ns)')
    a = 5; b=6
    print('scope: ', dir())
    print('locals: ', locals().keys())
    print('globals: ', globals().keys())
    print('a', a)

    def sub_local():
        print('-'*15)
        print('Lokalnie (sub_local)')
        print('scope: ', dir())
        print('locals: ', locals().keys())
        print('globals: ', globals().keys())
        # print('a', a)
        # # # wstrzykiwanie zmienneych
        # # global b
        # # b = 3
        # print('b', b)
    sub_local()
# wstrzykiwanie zmienneych
# print('global b', b)
local_local_ns()
# print('global b', b)
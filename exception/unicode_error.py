try:
    b'\x80'.decode("utf-8")
except UnicodeError as e:
    print(e)
    # noinspection PyUnresolvedReferences
    print(e.encoding)
    # noinspection PyUnresolvedReferences
    print(e.reason)
    # noinspection PyUnresolvedReferences
    print(e.object)
    # noinspection PyUnresolvedReferences
    print(e.start)
    # noinspection PyUnresolvedReferences
    print(e.end)

"""
'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
utf-8
invalid start byte
b'\x80'
0
1
"""

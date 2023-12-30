try:
    # noinspection PyUnresolvedReferences
    import AAA
except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)
    print(e.msg)

"""
("No module named 'AAA'",)
AAA
None
No module named 'AAA'
"""

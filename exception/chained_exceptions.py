a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    print(0 / 0)

"""
Traceback (most recent call last):
  File "/home/noritaka-izumi/sources/pcpp1-study/exception/chained_exceptions.py", line 4, in <module>
    print(a_list[3])
          ~~~~~~^^^
IndexError: list index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/noritaka-izumi/sources/pcpp1-study/exception/chained_exceptions.py", line 6, in <module>
    print(0 / 0)
          ~~^~~
ZeroDivisionError: division by zero
"""

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

personnel_check()

"""
Final check procedure
        The captain's name is John
        The pilot's name is Mary
        The mechanic's name is Mike
Traceback (most recent call last):
  File "/home/noritaka-izumi/sources/pcpp1-study/exception/explicitly_chained.py", line 10, in personnel_check
    print("\tThe navigator's name is", crew[3])
                                       ~~~~^^^
IndexError: list index out of range

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/noritaka-izumi/sources/pcpp1-study/exception/explicitly_chained.py", line 17, in <module>
    personnel_check()
  File "/home/noritaka-izumi/sources/pcpp1-study/exception/explicitly_chained.py", line 12, in personnel_check
    raise RocketNotReadyError('Crew is incomplete') from e
RocketNotReadyError: Crew is incomplete
"""

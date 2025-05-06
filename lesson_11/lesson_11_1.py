import math

def prime_generator(end: int):
  def prime(num: int) -> bool:

    if num <= 1:
      return False
    elif num == 2:
      return True
    elif num % 2 == 0:
      return False

    limit = int(math.sqrt(num))
    for i in range(3, limit + 1, 2):
      if num % i == 0:
        return False

    return True

  for n in range(2, end + 1):
    if prime(n):
      yield n

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')



from math import inf, sqrt
from typing import List

def hello(name = ""):
    if name == "":
        return "Hello!"
    return "Hello, "+ name + "!"


def int_to_roman(num: int) -> str:
    d = {1:'I',	4:'VI', 5:'V', 9:'XI', 10:'X', 40:'LX', 50:'L', 90:'CX', 100:'C', 400:'DC', 500:'D', 900:'MC', 1000:'M'}
    res = str()
    mult = 1
    while num:
        a = num % 10
        if a < 4:
            res += a * d[mult]
        elif a == 4:
            res += d[4 * mult]
        elif a == 9:
            res += d[9 * mult]
        else:
            res += (a - 5) * d[mult] + d[5 * mult]
        num //= 10
        mult *= 10
        
    return res[::-1]


def longest_common_prefix(strs_input: List[str]) -> str:
    if len(strs_input) == 0:
        return str()
    copy = list(map(lambda word: word.lstrip(), strs_input))
    for i in range (1, len(copy[0]) + 1):
        prefix = copy[0][0 : i]
        for word in copy:
            if word[0 : i] != prefix :
                return word[0 : i - 1]
    return copy[0]


def primes() -> int:
    n = 2
    while True:
        for k in range(2, int(sqrt(n)) + 1):
            if n % k == 0:
                break
        else:
            yield n
        n += 1


class BankCard:
    def __init__(self, total_sum: int, balance_limit = inf):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def foo(self, sum_spent):
        if self.total_sum < sum_spent:
            print(f"Can't spend {sum_spent} dollars")
            raise ValueError
        self.total_sum -= sum_spent
        print(f'You spent {sum_spent} dollars.')

    def __repr__(self):
        return 'To learn the balance call balance.'
    __call__ = foo

    @property
    def balance(self):
        if self.balance_limit < 1:
            print('Balance check limits exceeded.')
            raise ValueError
        self.balance_limit -= 1
        return self.total_sum

    def put(self, sum_put):
        self.total_sum += sum_put
        print(f'You put {sum_put} dollars.')

    def __add__(self, other):
        return BankCard(self.total_sum + other.total_sum, max(self.balance_limit, other.balance_limit))
        

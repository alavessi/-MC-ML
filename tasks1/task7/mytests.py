from task7 import find_shortest

print(find_shortest('eufhi uiewfhof fewiohidq  weqtq yefwgiqew gfyd fewff       fwew fgwereht '))
print(find_shortest('9230847;;;;1;;;++++_______a')) # 1

assert find_shortest(";123assdcdcef092101,3131313akdmkmedkfmwekfwe") == 9
assert find_shortest('tr9230847;;;;1;;;++++_______abbbbbbc') == 2
assert find_shortest("askdhrfef8wej9013d,kdj;12oid3fjvn23") == 1
assert find_shortest('9230847;;;;1;;;++++_______a') == 1
assert find_shortest('1ciwoeiworiworworow') == 18
assert find_shortest("aslkdjfhkssdf") == 13
assert find_shortest("ad2aaaaa,,bsc") == 2
assert find_shortest('12i330232l') == 1
assert find_shortest("111") == 0
assert find_shortest("+_*") == 0
assert find_shortest("") == 0
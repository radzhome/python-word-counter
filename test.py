#!/usr/bin/env python

"""
This is the "test" module.

This shows how a doc test can be used to test the module, e.g.

>>> wc = WordCounter("samples/test1.txt")
>>> wc.total_words
319
>>> wc.top_10
['sed', 'quis', 'eu', 'ip-sum', 'vel', 'et', 'ultricies', 'nunc', 'tortor', 'leo']


>>> wc = WordCounter("samples/test6.txt")
>>> wc.total_words
1095695

Below assert is used to check the expected values. Changing the expected values will show a fail.
The assertions are checked first.
"""
import doctest

from word_counter.counter import WordCounter

# Lorem ipsum file with hyphenated words
wc = WordCounter("samples/test1.txt")
assert wc.top_10 == ['sed', 'quis', 'eu', 'ip-sum', 'vel', 'et', 'ultricies', 'nunc', 'tortor', 'leo'], wc.top_10
assert wc.total_words == 319, wc.total_words

# Test basic punctuation
wc = WordCounter("samples/test2.txt")
assert wc.top_10 == ['this', 'is', 'and', 'test', 'simple', 'very', 'a'], wc.top_10
assert wc.total_words == 12, wc.total_words

# Test case sensitivity
wc = WordCounter("samples/test3.txt")
assert wc.top_10 == ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one'],  wc.top_10
assert wc.total_words == 16

# Test single line file
wc = WordCounter("samples/test3.txt")
assert wc.top_10 == ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
assert wc.total_words == 16

# Test empty file
wc = WordCounter("samples/test5.txt")
assert wc.top_10 == []
assert wc.total_words == 0

# Test large file
wc = WordCounter("samples/test6.txt")
assert wc.top_10 == ['the', 'of', 'and', 'to', 'in', 'a', 'he', 'that', 'was', 'his'], wc.top_10
assert wc.total_words == 1095695

# Test numbers
wc = WordCounter("samples/test7.txt")
assert wc.top_10 == ['69', '123', '567', '67', '45', '345'], wc.top_10
assert wc.total_words == 12


# Uncomment to run doc-test
# doctest.testmod()

print("Done!")

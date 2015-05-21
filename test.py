#!/usr/bin/env python

"""
This is the "test" module.

This shows how a doc test can be used to test the module, e.g.

>>> wc = WordCounter("samples/test1.txt")
>>> wc.total_words
310
>>> wc.top_10
['sed', 'quis', 'eu', 'vel', 'et', 'ultricies', 'nunc', 'tortor', 'leo', 'elit']


>>> wc = WordCounter("samples/test6.txt")
>>> wc.total_words
1095695

Below assert is used to check the expected values. Changing the expected values will show a fail.
The assertions are checked first.
"""

import doctest

from word_counter.counter import WordCounter

wc = WordCounter("samples/test1.txt")
assert wc.top_10 == ['sed', 'quis', 'eu', 'vel', 'et', 'ultricies', 'nunc', 'tortor', 'leo', 'elit']
assert wc.total_words == 310

wc = WordCounter("samples/test5.txt")
assert wc.top_10 == []
assert wc.total_words == 0

doctest.testmod()

print "No news is good news..."
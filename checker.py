"""
Auto checking for code challenge

https://devskiller.com/interview-coding-challenges/#3_How_hard_should_your_hiring_coding_interview_challenges_be

Additional questions:
- Read the instructions!
  - test suite included
  - did not use 3rd party modules
  - did not use any built in sorting or counting
- Understood the requirements,
- What technical decisions were made?
- Asked any questions? Any assumptions identified?
- What code coverage was achieved? (All functions tested?)
- What business rules/cases were covered? (All business cases?)
- How as storing top 10 achieved?
- What data structures were used to leverage sorting?
- Uniqueness of solution/problem solving i.e. regex, batch processing etc.
- Organization of code? OO, functional, easy to read/follow
- Defined the problem:
  - case sensitivity
  - dealing with punctuation
  - hyphenated words, numbers
"""
import subprocess

# TODO: Tailor the specific cases to exact test i.e. case sensitivity etc..

# run time and memory
output = subprocess.check_output(['/usr/bin/time', '-l', 'python3', 'word_counter.py', 'samples/test6.txt'])
print(output)  # look at "maximum resident set size" for memory and "real" for runtime

# 1st sample
output = subprocess.check_output(['python3', 'word_counter.py', 'samples/test1.txt'])
expected = b'Top 10 Words:\nsed 11\nipsum 9\nquis 9\neu 8\nip-sum 7\nvel 7\net 6\nultricies 5\nnunc 5\ntortor 5\nTotal Words: 326\n'
assert output == expected, f"Output: {output}, Expected {expected}"

# 2nd sample
output = subprocess.check_output(['python3', 'word_counter.py', 'samples/test2.txt'])
expected = b'Top 10 Words:\nthis 5\nis 2\nand 1\ntest 1\nsimple 1\nvery 1\na 1\nTotal Words: 12\n'
assert output == expected, f"Output: {output}, Expected {expected}"

# 3rd sample
output = subprocess.check_output(['python3', 'word_counter.py', 'samples/test3.txt'])
expected = b'Top 10 Words:\nthe 78735\nof 39973\nand 38068\nto 28579\nin 21715\na 20810\nhe 12114\nthat 12020\nwas 11361\nhis 10007\nTotal Words: 1095696\n'
assert output == expected, f"Output: {output}, Expected {expected}"

# 4th sample
output = subprocess.check_output(['python3', 'word_counter.py', 'samples/test4.txt'])
expected = b'Top 10 Words:\nten 6\nnine 1\neight 1\nseven 1\nsix 1\nfive 1\nfour 1\nthree 1\ntwo 1\none 1\nTotal Words: 16\n'
assert output == expected, f"Output: {output}, Expected {expected}"
import subprocess

# TODO: Tailor the specific cases to exact test i.e. case sensitivity etc..

# run time and memory
output = subprocess.check_output(['/usr/bin/time', '-l', 'python3', 'word_counter.py', 'samples/test6.txt'])
print(output)  # look at "maximum resident set size" for memory and "real" for runtime

# 1st sample
output = subprocess.check_output(['python3', 'word_counter.py', 'samples/test1.txt'])
expected = b'Top 10 Words:\nsed 11\nipsum 9\nquis 9\neu 8\nip-sum 7\nvel 7\net 6\nultricies 5\nnunc 5\ntortor 5\nTotal Words: 326\n'
assert output == expected, output


# 2nd
output = subprocess.check_output(['python3', 'word_counter.py', 'samples/test2.txt'])
expected = b'Top 10 Words:\nthis 5\nis 2\nand 1\ntest 1\nsimple 1\nvery 1\na 1\nTotal Words: 12\n'
assert output == expected, output

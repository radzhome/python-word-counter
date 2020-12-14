# python-word-counter
A python word counter, counts words in text files


### Objective ###

Create a simple application that takes a UTF-8 plain-text file as input and outputs:

* Total number of words in text file

* Ten most common words and number of occurrences for each

You application should be run from the command line using a single command. For example:

    $	python ./word_counter.py input.txt

Please include a test suite (tests.py) demonstrating the correctness of your solution and a README file clearly explaining how to build, run and test your application. 
DO NOT use `collections.Counter` or any built in sorting for this, please define your own counting and sorting instead. Please use python3 and best practices (PEP-8) to write your solution. Please include an explanation of your solution and any assumptions you made. Using an IDE like PyCharm is recommended, but not required.

The output should look as follows:

    Top 10 Words:
    the 78735
    of 39973
    and 38068
    to 28579
    in 21715
    a 20810
    he 12114
    that 12020
    was 11361
    his 10007
    Total Words: 1095695

### Usage ###

Run the main 'word_counter.py' file:

    ./word_counter.py samples/test1.txt


### Tests ###

Run the 'tests.py' test suite file:

    ./tests.py

### Install Globally ###

No setup is required. Either use the provided 'word_counter.py', or install and import the module:

    $ [sudo] setup.py install

### Discussion ###

* What is a word? An alphanumeric, numeric or alpha set of characters (minium 1), seperated by spaces, and punctuation is removed. Hyphenated words count as 1 i.e. `one-two` is 1 word, but `one two` is two. Punctuation such as `,\/*"'?!:` needs to be stripped away. Another scenario could be that we replace certain chars to make 1+ words out of a single word.
* In case of a tie between words, the word visited last (closest of EOF) will be bumped up in the list.
* Instead of sorting the frequencies at the end, a top 10 list keeps track of the most frequently occurring words
* For each word, up to 10 comparisons can be made, and the list needs to be shifted accordingly when an insert occurs
* This approach has a worst case scenario runtime of 0: n + 10n, which reduces to 0: n
* Another approach would be to sort at the end, and pick off the top 10 items, this would have a run time of  O: n*log(n) + n, which reduces to 0: n*log(n)
* Both approaches have a worst case space complexity of 0: n, if each word occurs only once.
* The assumption is that all the words can fit into memory, if this was not the case, reloads & preliminary writes to disk would be considered

### Input files testN.txt ###

 1. ip-sum x7 (different cases, hyphenated word), eu 8x (hyphenated case), ipsum different word
 1. punctuation test + case sensitivity, this x5
 1. ten x6 due to cases
 1. single word, 1 count
 1. 0 word case
 1. Large file, will it finish or crash? (no longer case with py3?)  (run with time -v or /usr/bin/time -l in osx) - See "maximum resident set size"
 1. Numbers - Number word count, 69 x4 , 123 x 3 .. Numbers always same case
 1. hyphenated words different from non-hyphenated - not implementing a dictionary so we should not base word boundaries based on definitions. If so is call made to api to distinguish the words?
 1. Input with file that does not exist, see if error is clear


### Typical issues ###

 * Hyphenated words counted as multiple words vs one word, should be one
 * Same word different cases or before comma, period, case sensitivity and punctuation
 * Large files, memory issues
 * Input with non-existent file FileNotFound or invalid file i.e jpeg - UnicodeDecodeError




# python-word-counter
A python word counter, counts words in a file


### Objective ###

Create a simple application that takes a UTF-8 plain-text file as input and outputs:

* Total number of words in text file

* Ten most common words and number of occurrences for each

You application should be run from the command line using a single command. For example:

    $	python	./word_counter.py	input.txt

    $	sbt	"run	input.txt"

Please include a test suite demonstrating the correctness of your solution and a README file clearly explaining how to build, run and test your application. DO NOT use `collections.Counter` for this, please define your own counter class instead. Please use python3 and best practices (PEP-8) to write your solution. Please include an explanation of your solution and any assumptions you made. 


### Usage ###

Run the included 'word_counter.py' file:

    ./word_counter.py samples/test1.txt


### Tests ###

Run the included 'test.py' file:

    ./test.py


### Discussion ###

* What is a word? An alphanumeric, numeric or alpha set of characters (minium 1), seperated by spaces, and puncuation is removed. Hyphenated words count as 1 i.e. `one-two` is 1 word, but `one two` is two. Punctuation such as `,\/*"'?!:` needs to be stripped away. Another scenario could be that we replace certain chars to make 1+ words out of a single word.
* In case of a tie between words, the word visited last (closest of EOF) will be bumped up in the list.
* Instead of sorting the frequencies at the end, a top 10 list keeps track of the most frequently occurring words
* For each word, up to 10 comparisons can be made, and the list needs to be shifted accordingly when an insert occurs
* This approach has a worst case scenario runtime of 0: n + 10n, which reduces to 0: n
* Another approach would be to sort at the end, and pick off the top 10 items, this would have a run time of  O: n*log(n) + n, which reduces to 0: n*log(n)
* Both approaches have a worst case space complexity of 0: n, if each word occurs only once.
* The assumption is that all the words can fit into memory, if this wasn't the case, reloads & preliminary writes to disk would be considered



### Install Globally ###

No setup is required. Either use the provided 'word_counter.py', or install and import the module:

    $ [sudo] setup.py install




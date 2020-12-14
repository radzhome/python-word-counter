#!/usr/bin/env python

import argparse

from word_counter.counter import WordCounter
from word_counter.counter import KEEP_TOP_WORDS


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Word counting program, counts frequency of words in a file.')
    parser.add_argument("file_path")

    args = parser.parse_args()
    if 'file_path' in args:
        file_path = True
    file_path = args.file_path

    wc = WordCounter(file_path)
    print(f"Top {KEEP_TOP_WORDS} Words:")
    wc.display_top_words()
    print("Total Words: {}".format(wc.total_words))

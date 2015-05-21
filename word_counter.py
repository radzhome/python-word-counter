#!/usr/bin/env python

import argparse

from word_counter.counter import WordCounter


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Word counting program, counts frequency of words in a file.')
    parser.add_argument("file_path")

    file_path = None
    args = parser.parse_args()
    if 'file_path' in args:
        file_path = True
    file_path = args.file_path

    wc = WordCounter(file_path)
    print "Top 10 Words:"
    wc.display_top_10()
    print "Total Words: {}".format(wc.total_words)
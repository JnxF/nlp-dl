#!/usr/bin/python3
import sys
import argparse


MAX_WINDOW = 5


def write_document(sentences):
    outfile = "chinesetext_segmented.utf8"
    with open(outfile, mode="w", encoding="utf8") as g:
        for sentence in sentences:
            g.write(sentence + "\n")


def segment(l, all_words):
    res = ""
    i = 0
    while i < len(l):
        chosen = None
        for window in reversed(range(MAX_WINDOW)):
            word = l[i : i + window]
            if word in all_words:
                chosen = word
                i += window
                break
        if not chosen:
            chosen = l[i]
            i += 1
        res += chosen + " "
    res = res.rstrip()
    return res


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} word-list-file unsegmented-text-file")
        return

    word_list_file = sys.argv[1]
    unsegmented_file = sys.argv[2]

    with open(word_list_file, "r", encoding="utf8") as word_list:
        with open(unsegmented_file, "r", encoding="utf8") as unsegmented:
            all_words = [line.rstrip() for line in word_list]
            sentences = [segment(l.rstrip(), all_words) for l in unsegmented]
            write_document(sentences)


if __name__ == "__main__":
    main()

import sys
import argparse
import codecs


def write_document(sentences):
    outfile = "chinesetext_segmented.utf8"
    g = codecs.open(outfile, mode="w", encoding="utf8")
    for sentence in sentences:
        g.write(sentence + "\n")
    g.close()


def segment(l, all_words):
    res = ""
    n = len(l)
    i = 0
    MAX_WINDOW = 5

    while i < n:
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

    word_list = codecs.open(word_list_file, mode="r", encoding="utf8")
    unsegmented = codecs.open(unsegmented_file, mode="r", encoding="utf8")

    all_words = [line.rstrip() for line in word_list]

    sentences = []
    for l in unsegmented:
        l = l.rstrip()
        segmented = segment(l, all_words)
        sentences.append(segmented)

    print("end")

    word_list.close()
    unsegmented.close()

    write_document(sentences)


if __name__ == "__main__":
    main()
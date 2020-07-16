from argparse import ArgumentParser
from conllu import parse_incr
from collections import defaultdict
import pickle
import os.path
from os import path


def compute_probabilities(file, regenerate=False):
    binary_probabilities = "probabilities.o"

    if regenerate or not path.exists(binary_probabilities):
        print("> Generating probabilities file")

        # Compute probabilities
        single_occurrences_pos = defaultdict(lambda: 0)
        pairs_consecutive_pos = defaultdict(lambda: 0)
        tag_transition_prob = defaultdict(lambda: 0)

        # Count
        with open(file, "r", encoding="utf-8") as fd:
            for sentence in parse_incr(fd):
                previous = None
                for word in sentence:
                    pos = word["upos"]
                    single_occurrences_pos[pos] += 1
                    if previous != None:
                        previous_pos = previous["upos"]
                        pairs_consecutive_pos[(previous_pos, pos)] += 1
                    previous = word

        # Calculate probabilities
        for pair, Cab in pairs_consecutive_pos.items():
            a, b = pair
            Ca = single_occurrences_pos[a]
            tag_transition_prob[(b, a)] = Cab / Ca

        tag_transition_prob = dict(tag_transition_prob)

        # Save to file
        with open(binary_probabilities, "wb") as fd:
            pickle.dump(tag_transition_prob, fd)

        print("< Finishing probabilities file")

    # Load file and return
    with open(binary_probabilities, "rb") as fd:
        return pickle.load(fd)


def ensure(probabilities, t1):
    d = {t: p for (t, previous), p in probabilities.items() if previous == t1}
    return sorted(d.items(), key=lambda x: -x[1])


def test_accuracy(test_file, probabilities):
    seen = 0
    correct = 0

    print("> Starting tests")
    with open(test_file, "r", encoding="utf-8") as tf:
        for sentence in parse_incr(tf):
            previous = None
            for word in sentence:
                if previous is not None:
                    previous_pos = previous["upos"]
                    pos = word["upos"]
                    possibilities = ensure(probabilities, previous_pos)
                    most_likely = possibilities[0][0]
                    if pos == most_likely:
                        correct += 1
                    seen += 1
                previous = word

    print("< Finishing tests")
    print()

    print(f"Total: {seen} words")
    print(f"Correct: {correct} PoS")
    print(f"Accuracy: {correct * 100 / seen} %")


if __name__ == "__main__":
    parser = ArgumentParser(description="POS tagger")
    parser.add_argument(
        "train_file", type=str, help="Path to the *.conllu training file"
    )
    parser.add_argument("test_file", type=str, help="Path to the *.conllu test file")
    parser.add_argument(
        "-f", "--force", help="Recomputes the probabilities file", action="store_true"
    )

    args = parser.parse_args()

    train_file = args.train_file
    test_file = args.test_file
    force = args.force

    probabilities = compute_probabilities(train_file, force)
    test_accuracy(test_file, probabilities)

import argparse

from trie import Trie

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, type=str)
parser.add_argument("--output", default="dictionary_TRIE.txt", type=str)
args = parser.parse_args()

trie = Trie()

with open(args.input, "r") as f:
    for line in f:
        line = line.strip()
        if line == "" or line[0] == "#":
            continue
        morphs = line.split("+")
        for morph in morphs:
            elem = morph.split("/")
            trie.insert(elem[0], elem[-1])

trie.show_all(args.output)

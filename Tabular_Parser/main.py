import argparse

from trie import Trie
from tabular_parser import TabularParser

def get_dictionary(args, trie):
    with open(args.input, "r") as f:
        for line in f:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue
            morphs = line.split("+")
            for morph in morphs:
                elem = morph.split("/")
                trie.insert(elem[0], elem[-1])

def get_grammar(args, filename):
    grammar = []
    with open(filename, "r") as f:
        for line in f:
            grammar.append(line.strip())
    return grammar

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument("--grammar", default="grammar.txt", type=str)
    args = parser.parse_args()

    # make TRIE dictionary
    trie = Trie()
    get_dictionary(args, trie)

    # make grammar
    grammar = get_grammar(args, args.grammar)

    # tabular parsing
    pos_parser = TabularParser(trie, grammar)
    with open(args.input, "r") as f:
        with open(f"pos_tagged_{args.input}", "w") as f_w:
            for line in f:
                words = line.strip().split(" ")
                if words[0] == "#":
                    f_w.write(line)
                    for word in words[1:]:
                        f_w.write(f"{pos_parser.parse(word)[0]}\n")
                    f_w.write("\n")


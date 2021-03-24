import argparse
import os

from tabular_parser import TabularParser
from trie import Trie


def get_dictionary(input_path, trie):
    with open(input_path, "r") as f:
        for line in f:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue
            morphs = line.split("+")
            for morph in morphs:
                elem = morph.split("/")
                trie.insert(elem[0], elem[-1])


def get_grammar(filename):
    grammar = []
    with open(filename, "r") as f:
        for line in f:
            grammar.append(line.strip())
    return grammar


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_name_or_path", required=True, type=str)
    parser.add_argument("--grammar_name_or_path", default="grammar.txt", type=str)
    parser.add_argument("--data_dir", default="data", type=str)
    args = parser.parse_args()

    input_path = os.path.join(args.data_dir, args.input_name_or_path)
    output_path = os.path.join(args.data_dir, f"pos_tagged_{args.input_name_or_path}")
    grammar_path = os.path.join(args.data_dir, args.grammar_name_or_path)

    # make TRIE dictionary
    trie = Trie()
    get_dictionary(input_path, trie)

    # make grammar
    grammar = get_grammar(grammar_path)

    # tabular parsing
    pos_parser = TabularParser(trie, grammar)
    with open(input_path, "r") as f:
        with open(output_path, "w") as f_w:
            for line in f:
                words = line.strip().split(" ")
                if words[0] == "#":
                    f_w.write(line)
                    for word in words[1:]:
                        f_w.write(f"{pos_parser.parse(word)[0]}\n")
                    f_w.write("\n")

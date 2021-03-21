import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, type=str)
parser.add_argument("--output", default="grammar.txt", type=str)
args = parser.parse_args()

grammar_list = [] # grammar list
with open(args.input, "r") as f:
    for line in f:
        line = line.strip()
        if line == "" or line[0] == "#":
            continue
        morphs = line.split("+")
        pos_list = []
        for morph in morphs:
            pos_list.append(morph.split("/")[-1])
        length = len(pos_list)
        for i in range(1, length):
            grammar = f"{pos_list[i-1]} {pos_list[i]}"
            if grammar not in grammar_list:
                grammar_list.append(grammar)

grammar_list.sort()
with open(args.output, "w") as f:
    for grammar in grammar_list:
        f.write(f"{grammar}\n")


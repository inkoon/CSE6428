from CKYParser import Cell, Constituent

def get_grammar(filename):
    grammar = dict()
    with open(filename, "r") as f:
        for line in f:
            tokens = line.strip().split("->")
            if len(tokens) != 2:
                continue
            lhs, rhs = tokens
            lhs = lhs.strip()
            rhs = rhs.strip()
            if rhs not in grammar:
                grammar[rhs] = list()
            grammar[rhs].append(lhs)
    return grammar

def get_input(filename):
    inputs = list()
    with open(filename, "r") as f:
        inputs = [line.strip() for line in f]
    return inputs

def init_table(words, grammar, length):
    table = [[Cell() for _ in range(length)] for _ in range(length + 1)]
    return table

def print_grammar(lhs, rhs, f_g):
    f_g.write(f"{lhs} -> {rhs}\n")

def merge_self(table, grammar, i, j, f_g):
    for cons in table[i][j].cons:
        if cons.lhs in grammar:
            for g in grammar[cons.lhs]:
                table[i][j].cons.append(Constituent(g, cons.lhs, left_cons=cons))
                print_grammar(g, cons.lhs, f_g)

def merge(table, grammar, i, j, k, f_g):
    for l_cons in table[k][j].cons:
        for r_cons in table[i][k].cons:
            x = f"{l_cons.lhs} {r_cons.lhs}"
            if x in grammar:
                for g in grammar[x]:
                    cons = Constituent(g, x, l_cons, r_cons)
                    table[i][j].cons.append(cons)
                    print_grammar(g, x, f_g)

def dfs(cell):
    if cell is None:
        return ""
    if cell.is_leaf():
        return f"({cell.lhs} {cell.rhs})"
    else:
        output = ""
        output += dfs(cell.left_cons)
        output += dfs(cell.right_cons)
        return f"({cell.lhs} {output})"

def print_parse_tree(table, length, f_o):
    for cons in table[length][0].cons:
        if cons.lhs == "S":
            f_o.write(dfs(cons) + "\n")
    f_o.write("\n")

def parsing(sent, grammar, f_g, f_o):
    words = sent.strip().split(" ")
    length = len(words)
    table = init_table(words, grammar, length)
    for i in range(1, length + 1):
        for j in range(i - 1, -1, -1):
            for k in range(j + 1, i + 1):
                if j+1 == i:
                    if words[i-1] in grammar:
                        for g in grammar[words[i-1]]:
                            cons = Constituent(g, words[i-1])
                            table[i][j].cons.append(cons)
                            print_grammar(g, words[i-1], f_g)
                if k == i:
                    merge_self(table, grammar, i, j, f_g)
                else:
                    merge(table, grammar, i, j, k, f_g)
    print_parse_tree(table, length, f_o)
    f_g.write("\n")

if __name__ == "__main__":
    grammar = get_grammar("grammar.txt")
    inputs = get_input("input.txt")
    with open("used_grammar.txt", "w") as f_g:
        with open("output.txt", "w") as f_o:
            for sent in inputs:
                f_o.write(sent + "\n")
                f_g.write(sent + "\n")
                parsing(sent, grammar, f_g, f_o)

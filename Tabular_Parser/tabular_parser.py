class TabularParser():
    def __init__(self, trie, grammar):
        self.trie = trie
        self.grammar = grammar
        self.result = [[]]

    def init(self, string, length):
        self.result = [[None for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if i <= j:
                    self.result[i][j] = self.trie.search(string[i:j+1])

    def show(self):
        n = len(self.result[0])
        for i in range(n):
            print(self.result[i])

    def get_pos(self, token):
        res = []
        for elem in token.split("+"):
            pos = elem.split("/")[-1]
            res.append(pos)
        return res

    def grammar_check(self, token1, token2):
        if f"{self.get_pos(token1)[-1]} {self.get_pos(token2)[0]}" in self.grammar:
            return True
        else:
            return False

    def merge(self, res1, res2):
        merge_res = []
        for token1 in res1:
            for token2 in res2:
                if self.grammar_check(token1, token2):
                    merge_res.append(f"{token1}+{token2}")
        return merge_res


    def parse(self, string):
        length = len(string)
        self.init(string, length)
        for i in range(1, length):
            for j in range(length-1, -1, -1):
                for k in range(j, i):
                    self.result[j][i] += self.merge(self.result[j][k], self.result[k+1][i])
        return self.result[0][length-1]

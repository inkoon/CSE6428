class Node(object):
    def __init__(self, key, word=None):
        self.key = key  # char key
        self.word = word  # word if leaf node else None
        self.pos = []  # pos if leaf node else None
        self.children = {}  # child node


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.all_node = []

    def insert(self, word, pos):
        current_node = self.head

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.word = word
        if pos not in current_node.pos:
            current_node.pos.append(pos)
        if f"{word}/{pos}" not in self.all_node:
            self.all_node.append(f"{word}/{pos}")

    def show_all(self, filename):
        self.all_node.sort()
        with open(filename, "w") as f:
            for word in self.all_node:
                f.write(f"{word}\n")

    def search(self, string):
        current_node = self.head
        res = []

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return res

        word = current_node.word
        if word:
            for pos in current_node.pos:
                res.append(f"{word}/{pos}")
            return res
        else:
            return res

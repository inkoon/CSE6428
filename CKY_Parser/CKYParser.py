class Cell():

    def __init__(self):
        self.cons = list()


class Constituent():

    def __init__(self, lhs, rhs, left_cons=None, right_cons=None):
        self.lhs = lhs
        self.rhs = rhs
        self.left_cons = left_cons
        self.right_cons= right_cons

    def is_leaf(self):
        if self.left_cons == None and self.right_cons == None:
            return True
        else:
            return False


""" node """


class Node():
    """ class node """

    def __init__(self, char=None, end=False):
        """ ctor """
        self.char = char
        self.childs = [None] * 26
        self.end = end

    def get(self, key):
        """ method for test """
        for c in self.childs:
            if c is not None:
                if key == c.char:
                    return True
        return False

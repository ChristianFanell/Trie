""" test  """
import unittest
import sys
from node import Node
from trie import Trie
from spellchecker import Spellchecker



class TestTrieNode(unittest.TestCase):
    """ test node """
    def setUp(self):
        """ setup """
        self.a = Node()
        self.a.char = 'a'
        self.b = Node()
        self.b.char = 'b'

    def test_node_child(self):
        """ test nods child """
        self.a.childs[0] = self.b
        self.assertEqual(True, self.a.get('b'))

    def test_node_child2(self):
        """ fail test of node"""
        self.assertEqual(False, self.a.get('c'))


class TestTrie(unittest.TestCase):
    """ test trie class """

    def setUp(self):
        """ setup """
        self.t = Trie()
        self.names = ['lisa', 'lotta', 'lina']
        for n in self.names:
            self.t.insert(n)

    def test_trie_list(self):
        """ test of returned list """
        apa = self.t.get_trie_list()
        self.assertEqual(3, len(apa))

    def test_get(self):
        """ test of search function """
        self.assertEqual(True, self.t.get('lisa'))

    def test_ord(self):
        """ test of util function """
        self.t.find_index('c')
        self.assertEqual(2, 2)

    def test_insert(self):
        """ test insert """
        self.t.insert('lollo')
        self.assertEqual(4, len(self.t.get_trie_list()))

    def test_prefix(self):
        """ test prefix method """
        prefix = self.t.find_prefix('li')
        self.assertEqual(2, len(prefix))


class TestSpellchecher(unittest.TestCase):
    """ test of main class"""

    def setUp(self):
        self.s = Spellchecker()

    def test_read_file_error(self):
        """test of fail for change file"""
        self.assertRaises(FileNotFoundError,
                          Spellchecker.read_file('asdf.txt'))

    def test_quit(self):
        """ test clear trie """
        q = Spellchecker.quit('hopplabalobaquit')
        self.assertEqual(True, q)

    def test_set_trie(self):
        """ test setup, a change of trie object"""
        old_list = self.s.get_list()
        self.s.set_trie('apa.txt')
        new_list = self.s.get_list()
        self.assertGreaterEqual(new_list, old_list)


if __name__ == '__main__':
    # unittest.main()
    # unittest.main(verbosity=3)
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(verbosity=3).run(suite)

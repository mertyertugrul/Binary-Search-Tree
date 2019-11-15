import unittest
from BinarySearchTree import *


class MyTestCase(unittest.TestCase):
    def test_BinarySearchTree(self):
        """
        Testing insert, look_up, remove and traverse functions
        :return: None
        """
        # insert function
        a = BinarySearchTree(9)
        a.insert(4)
        self.assertEqual(4, a.root.left.value)
        a.insert(6)
        self.assertEqual(6, a.root.left.right.value)
        a.insert(20)
        self.assertEqual(20, a.root.right.value)
        a.insert(617)
        self.assertEqual(617, a.root.right.right.value)
        a.insert(15)
        self.assertEqual(15, a.root.right.left.value)
        a.insert(1)
        self.assertEqual(1, a.root.left.left.value)

        # lookup
        self.assertEqual('20 is in leaf 1', a.look_up(20))

        # remove
        a.remove(1)
        self.assertEqual(None, a.root.left.left)
        a.insert(1)

        a.remove(15)
        self.assertEqual(None, a.root.right.left)
        a.insert(15)

        a.remove(617)
        self.assertEqual(None, a.root.right.right)
        a.insert(617)

        a.remove(20)
        self.assertEqual(617, a.root.right.value)

        a.remove(6)
        self.assertEqual(617, a.root.right.value)





if __name__ == '__main__':
    unittest.main()

import unittest
from GraphImplementation import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        myGraph = Graph()
        myGraph.add_vertex('0')
        myGraph.add_vertex('1')
        myGraph.add_vertex('2')
        myGraph.add_vertex('3')
        myGraph.add_vertex('4')
        myGraph.add_vertex('5')
        myGraph.add_vertex('6')
        myGraph.add_edge('3', '1')
        myGraph.add_edge('3', '4')
        myGraph.add_edge('4', '2')
        myGraph.add_edge('4', '5')
        myGraph.add_edge('1', '2')
        myGraph.add_edge('1', '0')
        myGraph.add_edge('0', '2')
        myGraph.add_edge('6', '5')
        out = "{'number_of_nodes': 0, 'adjacent_list': {'0': ['1', '2'], '1': ['3', '2', '0'], '2': ['4', '1', '0'], '3': ['1', '4'], '4': ['3', '2', '5'], '5': ['4', '6'], '6': ['5']}}"
        self.assertEqual(out, str(myGraph.__dict__))
        self.assertEqual("['1', '4']", str(myGraph.search('3')))



if __name__ == '__main__':
    unittest.main()

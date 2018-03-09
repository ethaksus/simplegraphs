import unittest
from simplegraphs.graphs import Vertice, DirectedEdge, UndirectedEdge, Graph

class TestEdges(unittest.TestCase):
    def test_undirected_edge(self):
        v1, v2 = Vertice(), Vertice()
        edge = UndirectedEdge(v1, v2)

        # Check vertice neigbors and edges.
        self.assertTrue(v2 in v1.neighbors)
        self.assertTrue(v2 in v1.outgoing)
        self.assertTrue(v2 in v1.incoming)
        self.assertTrue(edge in v1.edges)
        self.assertTrue(edge in v1.outgoing_edges)
        self.assertTrue(edge in v1.incoming_edges)

        self.assertTrue(v1 in v2.neighbors)
        self.assertTrue(v1 in v2.outgoing)
        self.assertTrue(v1 in v2.incoming)
        self.assertTrue(edge in v2.edges)
        self.assertTrue(edge in v2.outgoing_edges)
        self.assertTrue(edge in v2.incoming_edges)  

        # Test traversal
        self.assertEqual(v1, edge.traverse(v2))
        self.assertEqual(v2, edge.traverse(v1))

        # Test edge mapping
        self.assertEqual(edge, v1.edge(v2))
        self.assertEqual(edge, v2.edge(v1))

    def test_directed_edge(self):
        v1, v2 = Vertice(), Vertice()
        edge = DirectedEdge(v1, v2)
        
        # Check properties of edge.
        self.assertEqual(v1, edge.outgoing)
        self.assertEqual(v2, edge.incoming)

        # Check vertice neigbors and edges.
        self.assertTrue(v2 in v1.neighbors)
        self.assertTrue(v2 in v1.outgoing)
        self.assertFalse(v2 in v1.incoming)
        self.assertTrue(edge in v1.edges)
        self.assertTrue(edge in v1.outgoing_edges)
        self.assertFalse(edge in v1.incoming_edges)

        self.assertTrue(v1 in v2.neighbors)
        self.assertFalse(v1 in v2.outgoing)
        self.assertTrue(v1 in v2.incoming)
        self.assertTrue(edge in v2.edges)
        self.assertFalse(edge in v2.outgoing_edges)
        self.assertTrue(edge in v2.incoming_edges)  

        # Test traversal
        self.assertEqual(v2, edge.traverse())

        # Test edge mapping
        self.assertEqual(edge, v1.edge(v2))
        self.assertEqual(edge, v2.edge(v1))


class TestVertices(unittest.TestCase):
    def test_connect(self):
        v1, v2, v3 = Vertice(), Vertice(), Vertice()

        # Test undirected connect.
        v1.connect(v2)
        self.assertTrue(v1 in v2.neighbors and v1 in v2.incoming)
        self.assertTrue(v2 in v1.neighbors and v2 in v1.outgoing)

        # Test directed connect.
        v1.connect(v3, directed=True)
        self.assertTrue(v1 in v3.incoming and v1 not in v3.outgoing)
        self.assertTrue(v3 in v1.outgoing and v3 not in v3.incoming)
        

class TestIterators(unittest.TestCase):
    def test_breadth_first(self):
        root = Vertice('A')
        v1, v2, v3 = Vertice('B'), Vertice('C'), Vertice('D')
        last = Vertice('E')

        root.connect(v1)
        root.connect(v2)
        root.connect(v3)
        v1.connect(last)

        bfs = [v for v in root.bfs()]
        self.assertEqual(5, len(bfs))
        self.assertEqual(last, bfs[-1])

    def test_depth_first(self):
        root = Vertice('A')
        v1, v2, v3, v4 = Vertice('B'), Vertice('C'), Vertice('D'), Vertice('E')

        root.connect(v1)
        root.connect(v2)
        v1.connect(v3)
        v2.connect(v4)

        labels = [v.label for v in root.dfs()]
        valid1 = labels == ['A', 'B', 'D', 'C', 'E']
        valid2 = labels == ['A', 'C', 'E', 'B', 'D']
        self.assertTrue(valid1 or valid2)


class TestGraphs(unittest.TestCase):
    def test_sample(self):
        pass


if __name__ == '__main__':
    unittest.main()
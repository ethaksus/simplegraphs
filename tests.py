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
        

class TestGraphs(unittest.TestCase):
    def test_sample(self):
        pass


if __name__ == '__main__':
    unittest.main()
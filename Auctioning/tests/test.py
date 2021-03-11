import unittest

from Infrastructure import Infrastructure
from Node import *


class TestNode(unittest.TestCase):
    def createInfrastructure(self):
        nodex = Node("nodex", {"memory": 10})
        node1 = Node("node1", {"memory": 10})
        node2 = Node("node2", {"memory": 10})
        node3 = Node("node3", {"memory": 10})

        connections = [(("nodex", "node1"), 1),
                       (("node2", "nodex"), 2),
                       (("node2", "node3"), 3),
                       ]

        infrastructure = Infrastructure([nodex, node1, node2], connections)

        app = {}
        app["name"] = "app"
        app["tasks"] = [{"name": "T1", "requirements": {"memory": 1}},
                        {"name": "T2", "requirements": {"memory": 1}}
                        ]

        infrastructure.addApplication(app)
        node1.addTask("app", "T1")
        node2.addTask("app", "T2")

        return infrastructure


    def test_serialize(self):
        infrastructure = self.createInfrastructure()
        serialized = infrastructure.serialize()

        deserialized = Infrastructure([], [])
        deserialized.deserialize(serialized)

        self.assertEqual(len(infrastructure.nodes), len(deserialized.nodes))
        self.assertEqual(infrastructure.getNode("nodex").name, deserialized.getNode("nodex").name)
        self.assertEqual(infrastructure.getNode("nodex").resources, deserialized.getNode("nodex").resources)
        self.assertEqual(infrastructure.getNode("node1").tasks, deserialized.getNode("node1").tasks)

    def test_node_neighbours(self):
        infrastructure = self.createInfrastructure()
        neighbours = infrastructure.getNode("nodex").getNeighbours()
        #print(neighbours)
        self.assertTrue(("node1", 1) in neighbours)
        self.assertTrue(("node2", 2) in neighbours)
        self.assertEqual(len(neighbours), 2)

    def test_tasks(self):
        infrastructure = self.createInfrastructure()
        node1 = infrastructure.getNode("node1")

        self.assertIsNotNone(infrastructure.getApp("app"))
        self.assertIsNotNone(infrastructure.getTask("app", "T1"))
        self.assertEqual(infrastructure.getMappedNode("app", "T1").name, "node1")
        self.assertIsNone(infrastructure.getMappedNode("app", "UNKNOWN"))








if __name__ == '__main__':
    unittest.main()

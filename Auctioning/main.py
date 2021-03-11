from Node import *
from Task import *
from Application import *
from Infrastructure import *
from Node import *

import pprint

serialized = {
    "nodes": [
        {"name": "n1", "resources": {"memory": 10, "storage": 100},
         "deployed": [{"task": "T1", "application": "app1"}]},
        {"name": "n2", "resources": {"memory": 10, "storage": 100}},
        {"name": "n3", "resources": {"memory": 10, "storage": 100}}
    ],
    "connections": [
        (("n1", "n2"), 100),
        (("n1", "n3"), 100)
    ],
    "applications": [{"name": "app1", "tasks": [
        {"name": "T1", "requirements": {"memory": 1}},
        {"name": "T2", "depends": ["T1"], "requirements": {"memory": 1}}

    ]}]
}

pprint.pp(serialized)

app = {}
app["name"] = "app"
app["tasks"] = [{"name": "T1", "requirements": {"memory": 1}},
                {"name": "T2", "requirements": {"memory": 1}}
                ]

nodeX = Node("nx", {"memory": 10, "storage": 1000})
node1 = Node("n1", {"memory": 26, "storage": 1000})
node2 = Node("n2", {"memory": 15, "storage": 1000})
node3 = Node("n3", {"memory": 150, "storage": 1000})

connections = [(("nx", "n1"), 100),
               (("nx", "n2"), 50),
               (("nx", "n3"), 70)]

infrastructure = Infrastructure([node1, node2, node3, nodeX], connections)
infrastructure.addApplication(app)

print("-----")
serialized = infrastructure.serialize()
pprint.pp(serialized)
print("-----")
infrastructure.deserialize(serialized)

serialized = infrastructure.serialize()
pprint.pp(serialized)
print("-----")

# infrastructure.auction(app, nodeX)



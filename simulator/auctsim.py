from Node import *
from Task import *
from Application import *
from Infrastructure import *


class Simulator:
	def __init__(self):
		pass
		
	def simulate(self):
		pass
	
		

task1 = Task("t1", {"memory":10, "storage":100}, [])
task2 = Task("t2", {"memory":15, "storage":200}, [task1])
app = Application("app", [task1, task2])

nodeX = Node("nx", {"memory":10, "storage":1000})
node1 = Node("n1", {"memory":26, "storage":1000})
node2 = Node("n2", {"memory":15, "storage":1000})
node3 = Node("n3", {"memory":150, "storage":1000})
 
infrastructure = Infrastructure([node1, node2, node3, nodeX])
infrastructure.auction(app, nodeX)

sim = Simulator()
sim.simulate()

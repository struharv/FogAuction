from Node import *
import copy

class AuctioningNode(Node):
	def __init__(self, name, resources, infrastructure = None):
		 super().__init__(name, resources, infrastructure)
	
	@staticmethod
	def deserialize(serialized):
		return AuctioningNode(serialized["name"], copy.deepcopy(serialized["resources"]))
		 

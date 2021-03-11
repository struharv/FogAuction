import random
import copy
from AuctioningNode import *

class Infrastructure:
	def __init__(self, nodes, connections):
		self.addNodes(nodes)
		self.connections = connections
		self.applications = []
		
	def addApplication(self, application):
		self.applications += [application]
		
	def addNodes(self, nodes):
		self.nodes = nodes
		for node in nodes:
			node.infrastructure = self
				
	
	def getNodeByName(self, name):
		for node in self.nodes:
			if node.name == name:
				return node
		return None
	
	
	def serialize(self):
		result = {}
		
		# --- nodes
		result["nodes"] = []
		for node in self.nodes:
			result["nodes"] += [node.serialize()]
		
		# --- connections
		result["connections"] = copy.deepcopy(self.connections)
		result["applications"] = copy.deepcopy(self.applications)
		
		return result
	
	def deserialize(self, dsr):
		self.nodes = []		
		self.applications = []		
		self.connections = []		
		
		# --- nodes
		self.nodes = []		
		for node in dsr["nodes"]:
			self.nodes += [AuctioningNode.deserialize(node)]
		
		self.applications = copy.deepcopy(dsr["applications"])
		self.connections = copy.deepcopy(dsr["connections"])	

	
	def auction(self, application, node):
		offers = []
		for node in self.nodes:
			offers += [node.advertise(application)]
		
		print("offers", offers)
		#self.deploy(application, offers)
		self.randomFit(application, offers)
	
	def deploy(self, application, offers):
		tasks = application.getTasks()
	
	def placeTask(self, task, offerNode):
		tmp = []
		for offer in range(len(offerNode)):
			if not task in offerNode[offer]:
				offerNode[offer] = [-1]
		
	
		
	def randomFit(self, application, offers):
		tasks = application.getTasks()
		
		for t in range(len(tasks)):
			for node in offers:
				print(node)
				self.placeTask(t, node)	
				print(node)
				
			
			
		#randomOffer = random(offers)
			
	def comply(self, deployment):
		pass
	
	
	
	

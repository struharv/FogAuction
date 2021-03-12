import random
import copy
from Node import *

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

	def getTask(self, app, task):
		app = self.getApp(app)
		if app is None:
			return None

		for t in app["tasks"]:
			if t["name"] == task:
				return t

		return None

	def getMappedNode(self, app, task):
		for node in self.nodes:
			if (app, task) in node.tasks:
				return node

		return None

	def undeploy(self, app):
		for node in self.nodes:
			pass



	def getApp(self, app:str):
		for a in self.applications:
			if a["name"] == app:
				return a
		return None


	def getNode(self, name):
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
			n = Node.deserialize(node)
			n.setInfrastructure(self)
			self.nodes += [n]
		
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
	
	
	
	

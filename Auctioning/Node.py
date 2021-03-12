import copy

class Node:
	def __init__(self, name, resources, infrastructure = None):
		self.resources = resources
		self.tasks = []
		self.infrastructure = infrastructure
		self.name = name
		self.offers = []

	def deploy(self, tasks):
		self.tasks += [tasks]

	def addTask(self, app, task):
		self.tasks += [(app, task)]

	def setInfrastructure(self, infrastructure):
		self.setInfrastructure = infrastructure

	def getNeighbours(self):
		res = []
		for con in self.infrastructure.connections:
			edge = con[0]
			if edge[0] == self.name:
				res += [(edge[1], con[1])]

			if edge[1] == self.name:
				res += [(edge[0], con[1])]

		return res

	@staticmethod
	def deserialize(serialized):
		node = Node(serialized["name"], copy.deepcopy(serialized["resources"]))
		node.tasks = copy.deepcopy(serialized["tasks"])
		return node


	def serialize(self):
		snode = {}
		snode["name"] = self.name
		snode["resources"] = {}
			
		snode["resources"] = copy.deepcopy(self.resources)
		snode["tasks"] = copy.deepcopy(self.tasks)
		return snode	

	# Returns available resources
	def availableResources(self):
		available = {}
		for key in self.resources:
			#print(key, self.resources[key], self.used(key))
			available[key] = self.resources[key] - self.usedResource(key)
		
		return available
		
	#used resource (e.g., "memory")
	def availableResource(self, resource):
		return self.resources[resource] - self.usedResource(resource)


	def usedResource(self, resource):
		res = 0
		for task in self.tasks:
			definition = self.infrastructure.getTask(task[0], task[1])
			res += definition["requirements"][resource]
		return res
	
	
	def advertise(self, application):
		pass
	
	
	def createBid(self, tasks):
		print("createBid", self.availableResources())
		self.offers = []
		self.generateOffers([], tasks)
		
		return self.offers
		
	def _mappingRequires(self, offer):
		res = {}
		for resource in self.resources:
			total = 0
			for o in offer:
				task = self.infrastructure.getTask(o[0], o[1])
				total += task["requirements"][resource]

			res[resource] = total
		return res

	# check if the offer is valid
	def _checkMapping(self, offer):
		required = self._mappingRequires(offer)
		available = self.availableResources()

		for req in required:
			if required[req] > available[req]:
				return False

		return True
	
	def generateOffers(self, offer, tasks):
		
		# check exceeding
		if not self._checkMapping(offer):
			#print("EXCEEDED resource", offer, self.mappingRequires(application, offer))
			return

		# no more tasks
		if len(tasks) == 0:
			if len(offer) > 0:
				self.offers += [offer]
				print("offer", offer, self._mappingRequires(offer))
				#print(offer, self._mappingRequires(application, offer))
			
			return
		
		# add
		newoffer = copy.deepcopy(offer)
		newoffer += [tasks[0]]
		self.generateOffers(newoffer, tasks[1:])
		
		# dont add
		newoffer = copy.deepcopy(offer)
		self.generateOffers(newoffer, tasks[1:])

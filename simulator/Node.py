import copy

class Node:
	def __init__(self, name, resources, infrastructure):
		self.resources = resources
		self.tasks = []
		self.infrastructure = infrastructure
		self.name = name		
		
		self.offers = []
		
	
	
	
	def deploy(tasks):
		self.tasks += [tasks]
	
	def getNeighbours(self):
		for con in infrastructure.connections:
			pass
	
		return []
		

	def serialize(self):
		snode = {}
		snode["name"] = self.name
		snode["resources"] = {}
			
		for res in self.resources:
			snode["resources"][res] = self.resources[res]
		
		return snode	
	
	
	


		
	# Returns available resources
	def availableResources(self):
		available = {}
		for key in self.resources:
			#print(key, self.resources[key], self.used(key))
			available[key] = self.resources[key] - self.used(key)
		
		return available
		
	#used resource (e.g., "memory")
	def used(self, resource):
		res = 0
		for task in self.tasks:
			res += task[resource]  
		return res
	
	
	def advertise(self, application):
		pass
	
	
	def createBid(self, application):
		print("createBid", self.availableResources())
		self.offers = []
		self.generateOffers(application, [], range(len(application.getTasks())))
		
		return self.offers
		
	def _mappingRequires(self, application, mappedTasks):
		res = {}
		tasks = application.getTasks()
		for resource in self.resources:
			total = 0
			for t in mappedTasks:
				total += tasks[t].getRequirements()[resource]
			res[resource] = total
		return res
	
	def _checkMapping(self, application, mappedTasks):
		required = self._mappingRequires(application, mappedTasks)
		available = self.availableResources()
		
		for resource in self.resources:
			if required[resource] > available[resource]:
				return False 
		
		return True
	
	def generateOffers(self, application, offer, tasks):
		
		#check exceeding
		if not self._checkMapping(application, offer):
			#print("EXCEEDED resource", offer, self.mappingRequires(application, offer))
			return 
		
		
		if len(tasks) == 0:
			if len(offer) > 0:
				self.offers += [offer]
				print(offer, self._mappingRequires(application, offer))
			
			return
		
		# add
		newoffer = copy.deepcopy(offer)
		newoffer += [tasks[0]]
		self.generateOffers(application, newoffer, tasks[1:])
		
		# dont add
		newoffer = copy.deepcopy(offer)
		self.generateOffers(application, newoffer, tasks[1:])

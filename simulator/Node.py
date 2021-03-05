import copy

class Node:
	def __init__(self, name, resources):
		self.resources = resources
		self.tasks = []
		self.offers = []
	
	def deploy(tasks):
		self.tasks += [tasks]
	
	def availableResources(self):
		available = {}
		for key in self.resources:
			#print(key, self.resources[key], self.used(key))
			available[key] = self.resources[key] - self.used(key)
		
		return available
			
	def used(self, resource):
		res = 0
		for task in self.tasks:
			res += task[resource]  
		return res
	
	def advertise(self, application):
		print("advertise available", self.availableResources())
		self.offers = []
		self.generateOffers(application, [], [0, 1])
		
		return self.offers
		
	def mappingRequires(self, application, mappedTasks):
		res = {}
		tasks = application.getTasks()
		for resource in self.resources:
			total = 0
			for t in mappedTasks:
				total += tasks[t].getRequirements()[resource]
			res[resource] = total
		return res
	
	def checkMapping(self, application, mappedTasks):
		required = self.mappingRequires(application, mappedTasks)
		available = self.availableResources()
		
		for resource in self.resources:
			if required[resource] > available[resource]:
				return False 
		
		return True
		
	
	
	def generateOffers(self, application, offer, tasks):
		
		#check exceeding
		if not self.checkMapping(application, offer):
			#print("EXCEEDED resource", offer, self.mappingRequires(application, offer))
			return 
		
		
		if len(tasks) == 0:
			if len(offer) > 0:
				self.offers += [offer]
				print(offer, self.mappingRequires(application, offer))
			
			return
		
		# add
		newoffer = copy.deepcopy(offer)
		newoffer += [tasks[0]]
		self.generateOffers(application, newoffer, tasks[1:])
		
		# dont add
		newoffer = copy.deepcopy(offer)
		self.generateOffers(application, newoffer, tasks[1:])

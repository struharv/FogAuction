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
		

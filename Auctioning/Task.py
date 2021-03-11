class Task:
	def __init__(self, name, requirements):
		self.name = name
		self.requirements = requirements
	
	def getRequirements(self):
		return self.requirements

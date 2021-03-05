class Task:
	def __init__(self, name, requirements, dependencies):
		self.name = name
		self.requirements = requirements
		self.dependencies = dependencies
	
	def getRequirements(self):
		return self.requirements

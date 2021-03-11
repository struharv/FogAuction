class Application:
	def __init__(self, name, tasks, dependencies):
		self.name = name
		self.tasks = tasks
		self.dependencies = dependencies

	def getTasks(self):
		return self.tasks

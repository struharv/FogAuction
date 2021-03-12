class Utils:
    @staticmethod
    def appToTasks(application):
        res = []
        for t in application["tasks"]:
            res += [(application["name"], t["name"])]

        return res

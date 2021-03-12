from unittest import TestCase

from Utils import Utils


class TestUtils(TestCase):
    def test_app_to_tasks(self):
        app = {}
        app["name"] = "app"
        app["tasks"] = [{"name": "T1", "requirements": {"memory": 1}},
                        {"name": "T2", "requirements": {"memory": 1}}
                        ]

        result = Utils.appToTasks(app)
        self.assertIn(('app', 'T1'), result)
        self.assertIn(('app', 'T2'), result)
        self.assertEqual(len(result), 2)

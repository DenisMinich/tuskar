"""TasksPlan implementation"""
from tuskar import tasks_storage


class TasksPlan(object):
    def __init__(self):
        self._storage = tasks_storage.TasksStorage()

    def register_task(self, name, task):
        self._storage.add_task(name, task)

"""TasksStorage implementation"""
import collections


class TasksStorage(object):

    def __init__(self):
        self._tasks = collections.defaultdict(set)

    def add_task(self, name, task):
        self._tasks[name].add(task)

    def get_task(self, name, context):
        competing_tasks = self._tasks[name]
        suitable_tasks = {
            task for task in competing_tasks
            if task.check_conditions(context)}
        if len(suitable_tasks) == 0:
            raise ValueError("No suitable tasks found!")
        elif len(suitable_tasks) == 1:
            return suitable_tasks.pop()
        elif len(suitable_tasks) > 1:
            raise ValueError("More than 1 suitable task found!")

"""Engine implementation"""
import collections

from tuskar import tasks_plan


class Engine(object):

    _plans = collections.defaultdict(tasks_plan.TasksPlan)

    @classmethod
    def get_plan(cls, plan_name=None):
        return cls._plans[plan_name]

    @classmethod
    def register(cls, task_name, plan_name=None):
        def _actual_decorator(task):
            cls._plans[plan_name].register_task(task_name, task)
            return task
        return _actual_decorator

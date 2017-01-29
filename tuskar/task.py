class Task(object):
    conditions = dict()

    @classmethod
    def check_conditions(cls, context):
        return all(item in context.items() for item in cls.conditions.items())

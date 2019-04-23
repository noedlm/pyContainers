class stack:
    def __init__(self, values=[]):
        self.values = values

    def pop(self):
        return self.values

    def push(self, value):
        return value

    def isEmpty(self):
        return False

    def clear(self):
        return []
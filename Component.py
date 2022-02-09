"""
  Basic component class to dedicate different components
"""


class Component:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

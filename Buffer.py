"""
Buffer class, to contain two components as a queue for workstation
"""


class Buffer:
    # define the buffer type (through component) and produce a container
    def __init__(self, component):
        self.component_type = component
        self.components = []

    # get the buffer's component name. e.g.: c1, c2...
    def get_type_name(self):
        return self.component_type.get_name()

    # directly get the component type
    def get_components(self):
        return self.components

    # add real component into the buffer, max is 2
    def insert_component(self):
        if len(self.components) < 2:
            self.components.append(self.component_type)

    # dedicate whether the buffer is full
    def is_full(self):
        if len(self.components) == 2:
            return True
        return False

    # remove the first component in the buffer
    def remove_component(self):
        if len(self.components) != 0:
            return self.components.pop(0)

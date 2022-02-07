
class Buffer:

    def __init__(self, component):
        self.component_type = component
        self.components = []

    def get_type_name(self):
        return self.component_type.get_name()

    def get_components(self):
        return self.components

    def insert_component(self):
        if len(self.components) < 2:
            self.components.append(self.component_type)

    def is_full(self):
        if len(self.components) == 2:
            return True
        return False

    def remove_component(self):
        if len(self.components) != 0:
            return self.components.pop(0)

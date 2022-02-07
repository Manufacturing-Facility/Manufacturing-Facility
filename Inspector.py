from random import randrange


class Inspector:

    def __init__(self):
        self.buffers = []
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def add_buffer(self, buffer):
        self.buffers.append(buffer)

    def is_blocked(self, component):
        for buffer in self.buffers:
            if buffer.get_type_name() == component.get_name():
                if not buffer.is_full():
                    return False
            else:
                continue
        return True

    def send_component(self, component):
        self.get_shortest_buffer(component).insert_component()

    def get_shortest_buffer(self, component):
        shortest_queue_length = len(self.buffers[0].get_components())
        temp_buffer = self.buffers[0]
        for buffer in self.buffers:
            if buffer.get_type_name() == component.get_name():
                temp_length = len(buffer.get_components())
                if temp_length < shortest_queue_length:
                    shortest_queue_length = temp_length
                    temp_buffer = buffer
        return temp_buffer

    def inspection(self, component, time):
        while self.is_blocked(component):
            continue
        time.sleep(time * 60)
        self.send(component)

    # get random component for inspector
    def get_random_component_for_inspector(self):
        number = randrange(1000)
        return self.components[number % len(self.components)]
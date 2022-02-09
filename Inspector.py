from random import randrange
from decimal import *

from FileReader import insp1, insp22, insp23, get_random_data


class Inspector:

    def __init__(self):
        self.buffers = []
        self.components = []
        self.complete_timeline = []
        self.spare_complete_timeline = []
        self.complete_time=Decimal(0)

    def add_component(self, component):
        self.components.append(component)

    def add_buffer(self, buffer):
        self.buffers.append(buffer)

    def get_complete_timeline(self, spare):
        if spare:
            return self.spare_complete_timeline
        return self.complete_timeline

    def get_complete_time(self):
        return self.complete_time

    def is_blocked(self, component):
        for buffer in self.buffers:
            if buffer.get_type_name() == component.get_name():
                if not buffer.is_full():
                    return False
            else:
                continue
        return True

    def send_component(self, component):
        if not self.is_blocked(component):
            self.get_shortest_buffer(component).insert_component()
        else:
            print("The inspector is blocked")

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

    # get random component for inspector
    def get_random_component_for_inspector(self):
        number = randrange(1000)
        return self.components[number % len(self.components)]

    def get_new_inspect_time(self, current_time, component):
        if component.get_name() == "C1":
            data = insp1

        elif component.get_name == "C2":
            data = insp22
        else:
            data = insp23
        random = get_random_data(data)
        self.complete_time = current_time+random

        if component.get_name == "C3":
            self.spare_complete_timeline.append(random)
        else:
            self.complete_timeline.append(random)

    def process(self, current_time, component):
        if current_time<self.complete_time:
            print("The inspector is still working")
            return current_time
        self.get_new_inspect_time(current_time, component)
        return self.complete_time


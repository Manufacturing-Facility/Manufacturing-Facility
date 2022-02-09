from random import randrange
from decimal import *

from FileReader import insp1, insp22, insp23, get_random_data

"""
    Class Inspector to inspect components and send them into buffers
"""


class Inspector:

    # constructor to the inspector
    def __init__(self):
        self.buffers = []  # the buffer list to collect all related buffers
        self.components = []  # contain the component this inspector would check
        self.complete_timeline = []  # the complete time list to store inspection complete time
        self.spare_complete_timeline = []  # the same complete list but only for inspector 2 component 3
        self.complete_time = Decimal(0)  # the current/next check complete time

    # add component types for inspector to check
    def add_component(self, component):
        self.components.append(component)

    # add buffer into the buffers attribute
    def add_buffer(self, buffer):
        self.buffers.append(buffer)

    # getter for complete timeline (spare_complete_timeline for C3)
    def get_complete_timeline(self, spare):
        if spare:
            return self.spare_complete_timeline
        return self.complete_timeline

    # getter for complete time attribute
    def get_complete_time(self):
        return self.complete_time

    # check whether all related buffers are full. Is so, then the inspector is blocked
    def is_blocked(self, component):
        for buffer in self.buffers:
            if buffer.get_type_name() == component.get_name():
                if not buffer.is_full():
                    return False
            else:
                continue
        return True

    # send component to the buffer with the same type and the shortest component
    def send_component(self, component):
        if not self.is_blocked(component):
            self.get_shortest_buffer(component).insert_component()
        else:
            print("The inspector is blocked")

    # get the shortest same type buffer in the work station
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

    # get the new random inspect time, according to different component.
    # and also update the complete_timeline
    def get_new_inspect_time(self, current_time, component):
        if component.get_name() == "C1":
            data = insp1

        elif component.get_name == "C2":
            data = insp22
        else:
            data = insp23
        random = get_random_data(data)
        self.complete_time = current_time + random

        if component.get_name == "C3":
            self.spare_complete_timeline.append(random)
        else:
            self.complete_timeline.append(random)

    # the method to allow the inspector to process component. But need check whether the
    # inspector is still working on the last one at the given current time
    def process(self, current_time, component):
        if current_time < self.complete_time:
            print("The inspector is still working")
            return current_time
        self.get_new_inspect_time(current_time, component)
        return self.complete_time

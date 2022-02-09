import time
from decimal import Decimal
from threading import Thread

from FileReader import get_random_data


class WorkStation:

    def __init__(self, name, data):
        self.name = name
        self.buffers = []
        self.data = data
        self.completion_timeline = []
        self.complete_time = Decimal(0)

    def get_name(self):
        return self.name

    def get_data(self):
        return self.data

    def get_buffers(self):
        return self.buffers

    def add_buffer(self, buffer):
        self.buffers.append(buffer)

    def ready_to_assemble(self):
        for buffer in self.buffers:
            if len(buffer.get_components()) == 0:
                return False
        return True

    def assemble(self, current_time):
        random = get_random_data(self.data)
        self.completion_timeline.append(random)
        self.complete_time = current_time + random
        print("work station "+self.get_name()+" done assembling")
        for buffer in self.buffers:
            buffer.remove_component()
        if self.get_name() == "W1":
            print("new Product 1 created")
        elif self.get_name() == "W2":
            print("new Product 2 created")
        else:
            print("new Product 3 created")

    def process(self, current_time):
        if (not self.ready_to_assemble()) or current_time < self.complete_time:
            print("waiting for component or working")
            return current_time
        self.assemble(current_time)
        return self.complete_time

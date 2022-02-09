from decimal import Decimal

from FileReader import get_random_data

"""
Class WorkStation. The place to take inspected component from buffer 
and use them to produce products.
"""


class WorkStation:

    # initialize the attributes
    def __init__(self, name, data):
        self.name = name  # the workstation name
        self.buffers = []  # the buffers to store spare components
        self.data = data    # the data list to show the each products produce time
        self.completion_timeline = []   # the list to save all completion time when produced a product
        self.complete_time = Decimal(0) # the complete time for next/this product

    # getter for attribute name
    def get_name(self):
        return self.name

    # getter for attribute data
    def get_data(self):
        return self.data

    # getter for attribute buffers list
    def get_buffers(self):
        return self.buffers

    # add new buffer to the buffers list
    def add_buffer(self, buffer):
        self.buffers.append(buffer)

    # whether the buffers has enough component to assemble a new product
    def ready_to_assemble(self):
        for buffer in self.buffers:
            if len(buffer.get_components()) == 0:
                return False
        return True

    # the assemble procedure to take components in buffer and assemble into product
    def assemble(self, current_time):
        random = get_random_data(self.data)
        self.completion_timeline.append(random)
        self.complete_time = current_time + random
        print("work station " + self.get_name() + " done assembling")
        for buffer in self.buffers:
            buffer.remove_component()
        if self.get_name() == "W1":
            print("new Product 1 created")
        elif self.get_name() == "W2":
            print("new Product 2 created")
        else:
            print("new Product 3 created")

    # start the assemble process. Checks whether it is idle (no enough components) or busy first
    def process(self, current_time):
        if (not self.ready_to_assemble()) or current_time < self.complete_time:
            print("waiting for component or working")
            return current_time
        self.assemble(current_time)
        return self.complete_time

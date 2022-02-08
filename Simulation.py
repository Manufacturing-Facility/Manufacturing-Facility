from random import randrange

from Buffer import Buffer
from Component import Component
from Inspector import Inspector
from WorkStation import WorkStation


def read_from_file(file_name):
    time_data = []
    file = open("data/" + file_name, 'r')
    while 1:
        line = file.readline()
        if line.rstrip() == '':
            break
        time_data.append(float(line.rstrip()))
    return time_data


# read data from dat file
insp1 = read_from_file("servinsp1.dat")
insp22 = read_from_file("servinsp22.dat")
insp23 = read_from_file("servinsp23.dat")
ws1 = read_from_file("ws1.dat")
ws2 = read_from_file("ws2.dat")
ws3 = read_from_file("ws3.dat")


class Factory:

    def __init__(self):
        # create instances for three components
        self.c1 = Component("C1")
        self.c2 = Component("C2")
        self.c3 = Component("C3")

        # create instances for three workstations
        self.workstation1 = WorkStation("W1")
        self.workstation2 = WorkStation("W2")
        self.workstation3 = WorkStation("W3")

        # create instances for buffers
        # the two numbers x, y indicates the workstation number W(x) and component number C(y)
        self.buffer11 = Buffer(self.c1)
        self.buffer21 = Buffer(self.c1)
        self.buffer22 = Buffer(self.c2)
        self.buffer31 = Buffer(self.c1)
        self.buffer33 = Buffer(self.c3)

        # create instances for two inspectors
        self.inspector1 = Inspector()
        self.inspector2 = Inspector()

        # add buffers to the workstations
        self.workstation1.add_buffer(self.buffer11)
        self.workstation2.add_buffer(self.buffer21)
        self.workstation2.add_buffer(self.buffer22)
        self.workstation3.add_buffer(self.buffer31)
        self.workstation3.add_buffer(self.buffer33)

        # add components to different inspector
        self.inspector1.add_component(self.c1)
        self.inspector2.add_component(self.c2)
        self.inspector2.add_component(self.c3)

        # add buffers to different inspector
        self.inspector1.add_buffer(self.buffer11)
        self.inspector1.add_buffer(self.buffer21)
        self.inspector1.add_buffer(self.buffer31)
        self.inspector2.add_buffer(self.buffer22)
        self.inspector2.add_buffer(self.buffer33)

    def simulation(self):
        self.inspector1.inspection(self.c1, self.insp1.pop(0))


if __name__ == '__main__':
    factory = Factory()
    data = read_from_file("servinsp1.dat")
    print(data)

from decimal import Decimal

from Buffer import Buffer
from Component import Component
from FileReader import ws1, ws2, ws3
from Inspector import Inspector
from WorkStation import WorkStation

"""
Class Factory, to do the main simulation work, initialize the instances and run simulation
"""


class Factory:

    # initialize the Factory and create all instances.
    def __init__(self):
        # create instances for three components
        self.c1 = Component("C1")
        self.c2 = Component("C2")
        self.c3 = Component("C3")

        # create instances for three workstations
        self.workstation1 = WorkStation("W1", ws1)
        self.workstation2 = WorkStation("W2", ws2)
        self.workstation3 = WorkStation("W3", ws3)

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

    # simulate the whole simulation, need debug for future
    def simulation(self):
        current_time = Decimal(0)
        for x in range(10):
            if current_time >= self.inspector1.get_complete_time():
                component1 = self.inspector1.get_random_component_for_inspector()
                temp_time1 = self.inspector1.process(current_time, component1)
                print("after inspector1 process: " + str(temp_time1))
            else:
                print("Inspector 1 is still working")

            if current_time >= self.inspector2.get_complete_time():
                component2 = self.inspector2.get_random_component_for_inspector()
                temp_time2 = self.inspector2.process(current_time, component2)
                print("after inspector2 process: " + str(temp_time2))
            else:
                print("Inspector 2 is still working")

            temp_current_time = min(temp_time1, temp_time2)

            if temp_current_time == temp_time1:
                self.inspector1.send_component(component1)
            else:
                self.inspector2.send_component(component2)

            temp_ws1 = self.workstation1.process(temp_current_time)
            print("after ws1 process: " + str(temp_ws1))
            temp_ws2 = self.workstation2.process(temp_current_time)
            print("after ws2 process: " + str(temp_ws2))
            temp_ws3 = self.workstation3.process(temp_current_time)
            print("after ws3 process: " + str(temp_ws3))
            temp_times = [temp_time1, temp_time2, temp_ws1, temp_ws2, temp_ws3]
            temp_times.sort()
            if current_time != temp_current_time:
                for i in range(temp_times.count(temp_current_time) - 1):
                    temp_times.remove(temp_current_time)
                if temp_times[0] == temp_time1 or temp_times[0] == temp_time2:
                    current_time = temp_times[0]
                else:
                    current_time += temp_times[0]
            else:
                for i in range(temp_times.count(temp_current_time)):
                    temp_times.remove(temp_current_time)
                current_time = temp_times[0]

            print("\n\nnew current time is: " + str(current_time))


# main method to run the code
if __name__ == '__main__':
    factory = Factory()
    factory.simulation()

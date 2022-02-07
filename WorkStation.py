
class WorkStation:

    def __init__(self, name):
        self.name = name
        self.buffers = []

    def get_name(self):
        return self.name

    def get_buffers(self):
        return self.buffers

    def add_buffer(self, buffer):
        self.buffers.append(buffer)

    def ready_to_assemble(self):
        for buffer in self.buffers:
            if len(buffer.get_components()) == 0:
                return False
        return True

    def assemble(self):
        for buffer in self.buffers:
            buffer.remove_component()

    def process(self, time):
        while not self.ready_to_assemble():
            continue
        time.sleep(time * 60)
        self.assemble()

from pytia.framework.knowledge_interfaces.dimension import Dimension


class Angle(Dimension):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.angle = com_object

    def __repr__(self):
        return f'Angle(name="{ self.name }")'

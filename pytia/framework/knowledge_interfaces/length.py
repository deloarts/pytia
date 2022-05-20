from pytia.framework.knowledge_interfaces.dimension import Dimension


class Length(Dimension):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.length = com_object

    def __repr__(self):
        return f'Length(name="{ self.name }")'

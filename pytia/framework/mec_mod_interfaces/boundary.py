from pytia.framework.in_interfaces.reference import Reference


class Boundary(Reference):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.boundary = com_object

    def __repr__(self):
        return f'Boundary(name="{self.name}")'

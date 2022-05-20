from pytia.framework.system_interfaces.any_object import AnyObject


class Shape(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.shape = com_object

    def __repr__(self):
        return f'Shape(name="{self.name}")'

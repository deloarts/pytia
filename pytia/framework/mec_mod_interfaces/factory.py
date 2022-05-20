from pytia.framework.system_interfaces.any_object import AnyObject


class Factory(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.factory = com_object

    def __repr__(self):
        return f'Factory(name="{self.name}")'

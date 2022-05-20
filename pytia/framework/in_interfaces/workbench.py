from pytia.framework.system_interfaces.any_object import AnyObject


class Workbench(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.workbench = com_object

    def __repr__(self):
        return f'Workbench(name="{self.name}")'

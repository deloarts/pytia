from pytia.framework.system_interfaces.any_object import AnyObject


class TPSView(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tps_view = com_object

    def __repr__(self):
        return f'TPSView(name="{ self.name }")'

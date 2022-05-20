from pytia.framework.system_interfaces.any_object import AnyObject


class DefeaturingFilter(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing_filter = com_object

    def __repr__(self):
        return f'DefeaturingFilter(name="{self.name}")'

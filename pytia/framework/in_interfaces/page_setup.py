from pytia.framework.system_interfaces.any_object import AnyObject


class PageSetup(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.page_setup = com_object

    def __repr__(self):
        return f'PageSetup(name="{ self.name }")'

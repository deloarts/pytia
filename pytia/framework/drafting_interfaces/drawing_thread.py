from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.cat_types.general import cat_variant


class DrawingThread(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_thread = com_object

    @property
    def type(self) -> int:
        return self.drawing_thread.Type

    @type.setter
    def type(self, value: int):
        self.drawing_thread.Type = value

    def is_linked_to(self) -> cat_variant:
        return self.drawing_thread.IsLinkedTo()


def __repr__(self):
    return f'DrawingThread(name="{self.name}")'

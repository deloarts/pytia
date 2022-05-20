from pytia.framework.system_interfaces.any_object import AnyObject


class Camera(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.camera = com_object

    @property
    def type(self):
        return self.camera.Type

    def __repr__(self):
        return f'Camera(name="{ self.name }")'

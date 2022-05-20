from pytia.framework.system_interfaces.any_object import AnyObject


class LightSource(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.light_source = com_object

    def get_direction(self, o_direction: tuple) -> None:
        return self.light_source.GetDirection(o_direction)

    def put_direction(self, o_direction: tuple) -> None:
        return self.light_source.PutDirection(o_direction)

    def __repr__(self):
        return f'LightSource(name="{ self.name }")'

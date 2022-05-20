from pytia.framework.mec_mod_interfaces.shape import Shape


class DressUpShape(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dress_up_shape = com_object

    def __repr__(self):
        return f'DressUpShape(name="{self.name}")'

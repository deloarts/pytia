from pytia.framework.mec_mod_interfaces.shape import Shape


class TransformationShape(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.transformation_shape = com_object

    def __repr__(self):
        return f'TransformationShape(name="{ self.name }")'

from pytia.framework.system_interfaces.any_object import AnyObject


class ParticularTolElem(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.particular_tol_elem = com_object

    @property
    def particular_geometry(self) -> str:
        return self.particular_tol_elem.ParticularGeometry

    def __repr__(self):
        return f'ParticularTolElem(name="{ self.name }")'

from pytia.framework.system_interfaces.any_object import AnyObject


class ToleranceZone(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_zone = com_object

    @property
    def form(self) -> str:
        return self.tolerance_zone.Form

    @form.setter
    def form(self, value: str):
        self.tolerance_zone.Form = value

    @property
    def value(self) -> float:
        return self.tolerance_zone.Value

    @value.setter
    def value(self, value: float):
        self.tolerance_zone.Value = value

    def __repr__(self):
        return f'ToleranceZone(name="{ self.name }")'

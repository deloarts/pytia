from pytia.framework.system_interfaces.any_object import AnyObject


class Reference(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.reference = com_object

    @property
    def display_name(self) -> str:
        return self.reference.DisplayName

    def compose_with(self, i_reference: "Reference") -> "Reference":
        return Reference(self.reference.ComposeWith(i_reference.com_object))

    def __repr__(self):
        return f'Reference(name="{self.name}")'

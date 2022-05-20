from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.draft_domains import DraftDomains
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Draft(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.draft = com_object

    @property
    def draft_domains(self) -> DraftDomains:
        return DraftDomains(self.draft.DraftDomains)

    @property
    def mode(self) -> int:
        return self.draft.Mode

    @mode.setter
    def mode(self, value: int):
        self.draft.Mode = value

    @property
    def parting_element(self) -> Reference:
        return Reference(self.draft.PartingElement)

    @parting_element.setter
    def parting_element(self, value: Reference):
        self.draft.PartingElement = value

    def __repr__(self):
        return f'Draft(name="{self.name}")'

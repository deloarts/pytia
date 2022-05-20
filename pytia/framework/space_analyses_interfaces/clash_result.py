from pytia.framework.space_analyses_interfaces.conflicts import Conflicts
from pytia.framework.system_interfaces.any_object import AnyObject


class ClashResult(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.clash_result = com_object

    @property
    def conflicts(self) -> Conflicts:
        return Conflicts(self.clash_result.Conflicts)

    def export(self, i_type: int, i_path: str) -> None:
        return self.clash_result.Export(i_type, i_path)

    def __repr__(self):
        return f'ClashResult(name="{self.name}")'

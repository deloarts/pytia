from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class NonSemanticGDT(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_gdt = com_object

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.non_semantic_gdt.TPSParallelOnScreen())

    def __repr__(self):
        return f'NonSemanticGdt(name="{self.name}")'

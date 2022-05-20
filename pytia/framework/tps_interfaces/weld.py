from pytia.framework.drafting_interfaces.drawing_welding import DrawingWelding
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class Weld(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.weld = com_object

    def get_2d_annot(self) -> DrawingWelding:
        return DrawingWelding(self.weld.Get2dAnnot())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.weld.TPSParallelOnScreen())

    def __repr__(self):
        return f'Weld(name="{self.name}")'

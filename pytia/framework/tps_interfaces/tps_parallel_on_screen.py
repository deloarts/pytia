from pytia.framework.system_interfaces.any_object import AnyObject


class TPSParallelOnScreen(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tps_parallel_on_screen = com_object

    @property
    def parallel_on_screen(self) -> bool:
        return self.tps_parallel_on_screen.ParallelOnScreen

    @parallel_on_screen.setter
    def parallel_on_screen(self, value: bool):
        self.tps_parallel_on_screen.ParallelOnScreen = value

    @property
    def zoomable(self) -> bool:
        return self.tps_parallel_on_screen.Zoomable

    @zoomable.setter
    def zoomable(self, value: bool):
        self.tps_parallel_on_screen.Zoomable = value

    def __repr__(self):
        return f'TpsParallelOnScreen(name="{self.name}")'

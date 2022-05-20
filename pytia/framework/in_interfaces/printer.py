from pytia.framework.system_interfaces.any_object import AnyObject


class Printer(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.printer = com_object

    @property
    def device_name(self) -> str:
        return self.printer.DeviceName

    @property
    def orientation(self) -> int:
        return self.printer.Orientation

    @property
    def paper_height(self) -> float:
        return self.printer.PaperHeight

    @property
    def paper_size(self) -> int:
        return self.printer.PaperSize

    @property
    def paper_width(self) -> float:
        return self.printer.PaperWidth

    def __repr__(self):
        return f'Printer(name="{ self.name }")'

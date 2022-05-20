from pytia.framework.sketcher_interfaces.geometric_element import GeometricElement


class Geometry2D(GeometricElement):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.geometry_2d = com_object

    @property
    def construction(self) -> bool:
        return self.geometry_2d.Construction

    @construction.setter
    def construction(self, value: bool):
        self.geometry_2d.Construction = value

    @property
    def report_name(self) -> int:
        return self.geometry_2d.ReportName

    @report_name.setter
    def report_name(self, value: int):
        self.geometry_2d.ReportName = value

    def __repr__(self):
        return f'Geometry2D(name="{self.name}")'

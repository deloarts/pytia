from pytia.framework.sketcher_interfaces.geometry_2D import Geometry2D
from pytia.framework.sketcher_interfaces.line_2D import Line2D
from pytia.framework.sketcher_interfaces.point_2D import Point2D


class Axis2D(Geometry2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.axis_2d = com_object

    @property
    def horizontal_reference(self) -> Line2D:
        return Line2D(self.axis_2d.HorizontalReference)

    @property
    def origin(self) -> Point2D:
        return Point2D(self.axis_2d.Origin)

    @property
    def vertical_reference(self) -> Line2D:
        return Line2D(self.axis_2d.VerticalReference)

    def __repr__(self):
        return f'Axis2D(name="{self.name}")'

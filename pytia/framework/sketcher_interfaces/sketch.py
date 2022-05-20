from pytia.framework.mec_mod_interfaces.constraints import Constraints
from pytia.framework.mec_mod_interfaces.geometric_elements import GeometricElements
from pytia.framework.sketcher_interfaces.axis_2D import Axis2D
from pytia.framework.sketcher_interfaces.factory_2D import Factory2D
from pytia.framework.sketcher_interfaces.line_2D import Line2D
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService


class Sketch(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.sketch = com_object

    @property
    def absolute_axis(self) -> Axis2D:
        return Axis2D(self.sketch.AbsoluteAxis)

    @property
    def center_line(self) -> Line2D:
        return Line2D(self.sketch.CenterLine)

    @center_line.setter
    def center_line(self, value: Line2D):
        self.sketch.CenterLine = value

    @property
    def constraints(self) -> Constraints:
        return Constraints(self.sketch.Constraints)

    @property
    def factory_2d(self) -> Factory2D:
        return Factory2D(self.sketch.Factory2D)

    @property
    def geometric_elements(self) -> GeometricElements:
        return GeometricElements(self.sketch.GeometricElements)

    def close_edition(self) -> None:
        return self.sketch.CloseEdition()

    def evaluate(self) -> None:
        return self.sketch.Evaluate()

    def get_absolute_axis_data(self) -> tuple:
        vba_function_name = "get_absolute_axis_data"
        vba_code = """
        Public Function get_absolute_axis_data(sketch)
            Dim oAxisData(8)
            sketch.GetAbsoluteAxisData oAxisData
            get_absolute_axis_data = oAxisData
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def inverse_orientation(self) -> None:
        return self.sketch.InverseOrientation()

    def open_edition(self) -> Factory2D:
        return Factory2D(self.sketch.OpenEdition())

    def set_absolute_axis_data(self, i_axis_data: tuple) -> None:
        return self.sketch.SetAbsoluteAxisData(i_axis_data)

    def __repr__(self):
        return f'Sketch(name="{self.name}")'

from typing import Tuple

from pytia.framework.drafting_interfaces.drawing_dim_ext_line import DrawingDimExtLine
from pytia.framework.drafting_interfaces.drawing_dim_line import DrawingDimLine
from pytia.framework.drafting_interfaces.drawing_dim_value import DrawingDimValue
from pytia.framework.knowledge_interfaces.parameters import Parameters
from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingDimension(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dimension = com_object

    @property
    def cumulate_mode(self) -> bool:
        return self.drawing_dimension.CumulateMode

    @property
    def dim_status(self) -> int:
        return self.drawing_dimension.DimStatus

    @property
    def dim_type(self) -> int:
        return self.drawing_dimension.DimType

    @property
    def dual_value(self) -> int:
        return self.drawing_dimension.DualValue

    @dual_value.setter
    def dual_value(self, value: int):
        self.drawing_dimension.DualValue = value

    @property
    def forshortened(self) -> bool:
        return self.drawing_dimension.Forshortened

    @forshortened.setter
    def forshortened(self, value: bool):
        self.drawing_dimension.Forshortened = value

    @property
    def half_dim_mode(self) -> bool:
        return self.drawing_dimension.HalfDimMode

    @half_dim_mode.setter
    def half_dim_mode(self, value: bool):
        self.drawing_dimension.HalfDimMode = value

    @property
    def is_clipped(self) -> bool:
        return self.drawing_dimension.IsClipped

    @property
    def nb_ext_line(self) -> int:
        return self.drawing_dimension.NbExtLine

    @property
    def nb_symb(self) -> int:
        return self.drawing_dimension.NbSymb

    @property
    def parameters(self) -> Parameters:
        return Parameters(self.drawing_dimension.Parameters)

    @property
    def symbols_side(self) -> int:
        return self.drawing_dimension.SymbolsSide

    @symbols_side.setter
    def symbols_side(self, value: int):
        self.drawing_dimension.SymbolsSide = value

    @property
    def true_dim_mode(self) -> bool:
        return self.drawing_dimension.TrueDimMode

    @property
    def value_angle(self) -> float:
        return self.drawing_dimension.ValueAngle

    @value_angle.setter
    def value_angle(self, value: float):
        self.drawing_dimension.ValueAngle = value

    @property
    def value_auto_mode(self) -> int:
        return self.drawing_dimension.ValueAutoMode

    @value_auto_mode.setter
    def value_auto_mode(self, value: int):
        self.drawing_dimension.ValueAutoMode = value

    @property
    def value_display(self) -> int:
        return self.drawing_dimension.ValueDisplay

    @value_display.setter
    def value_display(self, value: int):
        self.drawing_dimension.ValueDisplay = value

    @property
    def value_frame(self) -> int:
        return self.drawing_dimension.ValueFrame

    @value_frame.setter
    def value_frame(self, value: int):
        self.drawing_dimension.ValueFrame = value

    @property
    def value_in_out(self) -> int:
        return self.drawing_dimension.ValueInOut

    @value_in_out.setter
    def value_in_out(self, value: int):
        self.drawing_dimension.ValueInOut = value

    @property
    def value_orientation(self) -> int:
        return self.drawing_dimension.ValueOrientation

    @value_orientation.setter
    def value_orientation(self, value: int):
        self.drawing_dimension.ValueOrientation = value

    @property
    def value_reference(self) -> int:
        return self.drawing_dimension.ValueReference

    @value_reference.setter
    def value_reference(self, value: int):
        self.drawing_dimension.ValueReference = value

    def get_boundary_box(self, o_values: tuple) -> None:
        return self.drawing_dimension.GetBoundaryBox(o_values)

    def get_clip(self, x: float, y: float, o_kept_side: int) -> None:
        return self.drawing_dimension.GetClip(x, y, o_kept_side)

    def get_dim_ext_line(self) -> DrawingDimExtLine:
        return DrawingDimExtLine(self.drawing_dimension.GetDimExtLine())

    def get_dim_line(self) -> DrawingDimLine:
        return DrawingDimLine(self.drawing_dimension.GetDimLine())

    def get_tolerances(self) -> Tuple[int, str, str, str, float, float, int]:
        vba_function_name = "get_tolerances"
        vba_code = """
        Public Function get_tolerances(drawing_dimension)
            Dim oValues(7)
            drawing_dimension.GetTolerances tol_type, tol_name, tol_up_s, tol_low_s, tol_up_d, tol_low_d, tol_display

            oValues(0) = tol_type
            oValues(1) = tol_name
            oValues(2) = tol_up_s
            oValues(3) = tol_low_s
            oValues(4) = tol_up_d
            oValues(5) = tol_low_d
            oValues(6) = tol_display

            get_tolerances = oValues
        End Function
        """
        value = self.application.system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )
        return value[0], value[1], value[2], value[3], value[4], value[5], value[6]

    def get_value(self) -> DrawingDimValue:
        return DrawingDimValue(self.drawing_dimension.GetValue())

    def move_value(
        self, x: float, y: float, sub_part: int, dim_angle_behavior: int
    ) -> None:
        return self.drawing_dimension.MoveValue(x, y, sub_part, dim_angle_behavior)

    def restore_value_position(self) -> None:
        return self.drawing_dimension.RestoreValuePosition()

    def set_clip(self, x: float, y: float, i_kept_side: int) -> None:
        return self.drawing_dimension.SetClip(x, y, i_kept_side)

    def set_tolerances(
        self,
        i_tol_type: int,
        itol_name: str,
        i_up_tol: str,
        i_low_tol: str,
        id_up_tol: float,
        id_low_tol: float,
        display_mode: int,
    ) -> None:
        return self.drawing_dimension.SetTolerances(
            i_tol_type,
            itol_name,
            i_up_tol,
            i_low_tol,
            id_up_tol,
            id_low_tol,
            display_mode,
        )

    def unclip(self) -> None:
        return self.drawing_dimension.Unclip()

    def __repr__(self):
        return f'DrawingDimension(name="{self.name}")'

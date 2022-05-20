from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingDimValue(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dim_value = com_object

    @property
    def fake_dim_type(self) -> int:
        return self.drawing_dim_value.FakeDimType

    @fake_dim_type.setter
    def fake_dim_type(self, value: int):
        self.drawing_dim_value.FakeDimType = value

    @property
    def scoring_mode(self) -> int:
        return self.drawing_dim_value.ScoringMode

    @scoring_mode.setter
    def scoring_mode(self, value: int):
        self.drawing_dim_value.ScoringMode = value

    @property
    def value(self) -> float:
        return self.drawing_dim_value.Value

    @property
    def value_framed_element(self) -> int:
        return self.drawing_dim_value.ValueFramedElement

    @value_framed_element.setter
    def value_framed_element(self, value: int):
        self.drawing_dim_value.ValueFramedElement = value

    @property
    def value_framed_group(self) -> int:
        return self.drawing_dim_value.ValueFramedGroup

    @value_framed_group.setter
    def value_framed_group(self, value: int):
        self.drawing_dim_value.ValueFramedGroup = value

    def get_bault_text(
        self, i_index: int, o_before: str, o_after: str, o_upper: str, o_lower: str
    ) -> None:
        return self.drawing_dim_value.GetBaultText(
            i_index, o_before, o_after, o_upper, o_lower
        )

    def get_display_unit(self, i_index: int) -> int:
        return self.drawing_dim_value.GetDisplayUnit(i_index)

    def get_fake_dim_value(self, i_index: int) -> str:
        return self.drawing_dim_value.GetFakeDimValue(i_index)

    def get_format_display_factor(self, i_index: int) -> int:
        return self.drawing_dim_value.GetFormatDisplayFactor(i_index)

    def get_format_name(self, i_index: int) -> str:
        return self.drawing_dim_value.GetFormatName(i_index)

    def get_format_precision(self, index: int) -> float:
        return self.drawing_dim_value.GetFormatPrecision(index)

    def get_format_type(self, i_index: int) -> int:
        return self.drawing_dim_value.GetFormatType(i_index)

    def get_format_unit(self, i_index: int) -> int:
        return self.drawing_dim_value.GetFormatUnit(i_index)

    def get_ps_text(self, i_index: int, o_prefix: str, o_suffix: str) -> None:
        return self.drawing_dim_value.GetPSText(i_index, o_prefix, o_suffix)

    def get_scored_element(self, i_index: int) -> bool:
        return self.drawing_dim_value.GetScoredElement(i_index)

    def set_bault_text(
        self, i_index: int, i_before: str, i_after: str, i_upper: str, i_lower: str
    ) -> None:
        return self.drawing_dim_value.SetBaultText(
            i_index, i_before, i_after, i_upper, i_lower
        )

    def set_fake_dim_value(self, i_index: int, i_fake_dim_value: str) -> None:
        return self.drawing_dim_value.SetFakeDimValue(i_index, i_fake_dim_value)

    def set_format_display_factor(self, i_index: int, i_frm_dsp_fact: int) -> None:
        return self.drawing_dim_value.SetFormatDisplayFactor(i_index, i_frm_dsp_fact)

    def set_format_name(self, i_index: int, i_frm_name: str) -> None:
        return self.drawing_dim_value.SetFormatName(i_index, i_frm_name)

    def set_format_precision(self, i_index: int, i_frm_precision: float) -> None:
        return self.drawing_dim_value.SetFormatPrecision(i_index, i_frm_precision)

    def set_format_type(self, i_index: int, i_frm_type: int) -> None:
        return self.drawing_dim_value.SetFormatType(i_index, i_frm_type)

    def set_format_unit(self, i_index: int, i_frm_unit: int) -> None:
        return self.drawing_dim_value.SetFormatUnit(i_index, i_frm_unit)

    def set_ps_text(self, i_index: int, i_prefix: str, i_suffix: str) -> None:
        return self.drawing_dim_value.SetPSText(i_index, i_prefix, i_suffix)

    def set_scored_element(self, i_index: int, i_scored_element: bool) -> None:
        return self.drawing_dim_value.SetScoredElement(i_index, i_scored_element)

    def __repr__(self):
        return f'DrawingDimValue(name="{ self.name }")'

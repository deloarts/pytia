from pytia.framework.system_interfaces.any_object import AnyObject


class VisPropertySet(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.vis_property_set = com_object

    def get_layer(self) -> tuple:
        return self.vis_property_set.GetLayer()

    def get_pick(self) -> int:
        return self.vis_property_set.GetPick()

    def get_real_color(self) -> tuple:
        return self.vis_property_set.GetRealColor()

    def get_real_inheritance(self) -> tuple:
        return self.vis_property_set.GetRealInheritance()

    def get_real_line_type(self) -> int:
        return self.vis_property_set.GetRealLineType()

    def get_real_opacity(self) -> int:
        return self.vis_property_set.GetRealOpacity()

    def get_real_width(self) -> int:
        return self.vis_property_set.GetRealWidth()

    def get_show(self) -> int:
        return self.vis_property_set.GetShow()

    def get_symbol_type(self) -> int:
        return self.vis_property_set.GetSymbolType()

    def get_visible_color(self) -> int:
        return self.vis_property_set.GetVisibleColor()

    def get_visible_inheritance(self) -> int:
        return self.vis_property_set.GetVisibleInheritance()

    def get_visible_line_type(self) -> int:
        return self.vis_property_set.GetVisibleLineType()

    def get_visible_opacity(self) -> int:
        return self.vis_property_set.GetVisibleOpacity()

    def get_visible_width(self) -> int:
        return self.vis_property_set.GetVisibleWidth()

    def set_layer(self, i_layer_type: int, i_layer_value: int) -> None:
        return self.vis_property_set.SetLayer(i_layer_type, i_layer_value)

    def set_pick(self, i_pick: int) -> None:
        return self.vis_property_set.SetPick(i_pick)

    def set_real_color(
        self, i_red: int, i_green: int, i_blue: int, i_inheritance: int
    ) -> None:
        return self.vis_property_set.SetRealColor(i_red, i_green, i_blue, i_inheritance)

    def set_real_line_type(self, i_line_type: int, i_inheritance: int) -> None:
        return self.vis_property_set.SetRealLineType(i_line_type, i_inheritance)

    def set_real_opacity(self, i_opacity: int, i_inheritance: int) -> None:
        return self.vis_property_set.SetRealOpacity(i_opacity, i_inheritance)

    def set_real_width(self, i_line_width: int, i_inheritance: int) -> None:
        return self.vis_property_set.SetRealWidth(i_line_width, i_inheritance)

    def set_show(self, i_show: int) -> None:
        return self.vis_property_set.SetShow(i_show)

    def set_symbol_type(self, i_symbol_type: int) -> None:
        return self.vis_property_set.SetSymbolType(i_symbol_type)

    def __repr__(self):
        return f'VisPropertySet(name="{self.name}")'

from pytia.framework.cat_types.general import cat_variant
from pytia.framework.system_interfaces.any_object import AnyObject


class AnalysisMaterial(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_material = com_object

    def get_type(self) -> str:
        return self.analysis_material.GetType()

    def get_value(self, i_label: str) -> cat_variant:
        return self.analysis_material.GetValue(i_label)

    def put_value(self, i_label: str, i_value: cat_variant) -> None:
        return self.analysis_material.PutValue(i_label, i_value)

    def __repr__(self):
        return f'AnalysisMaterial(name="{ self.name }")'

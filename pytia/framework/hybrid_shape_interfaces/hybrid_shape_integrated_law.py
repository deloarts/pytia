from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeIntegratedLaw(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_integrated_law = com_object

    @property
    def advanced_law(self) -> Reference:
        return Reference(self.hybrid_shape_integrated_law.AdvancedLaw)

    @advanced_law.setter
    def advanced_law(self, reference_law: Reference):
        self.hybrid_shape_integrated_law.AdvancedLaw = reference_law.com_object

    @property
    def end_param(self) -> Length:
        return Length(self.hybrid_shape_integrated_law.EndParam)

    @property
    def implicit_law_interpolation_mode(self) -> int:
        return self.hybrid_shape_integrated_law.ImplicitLawInterpolationMode

    @implicit_law_interpolation_mode.setter
    def implicit_law_interpolation_mode(self, value: int):
        self.hybrid_shape_integrated_law.ImplicitLawInterpolationMode = value

    @property
    def invert_mapping_law(self) -> bool:
        return self.hybrid_shape_integrated_law.InvertMappingLaw

    @invert_mapping_law.setter
    def invert_mapping_law(self, value: bool):
        self.hybrid_shape_integrated_law.InvertMappingLaw = value

    @property
    def pitch_law_type(self) -> int:
        return self.hybrid_shape_integrated_law.PitchLawType

    @pitch_law_type.setter
    def pitch_law_type(self, value: int):
        self.hybrid_shape_integrated_law.PitchLawType = value

    @property
    def spine(self) -> Reference:
        return Reference(self.hybrid_shape_integrated_law.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        self.hybrid_shape_integrated_law.Spine = reference_spine.com_object

    @property
    def start_param(self) -> Length:
        return Length(self.hybrid_shape_integrated_law.StartParam)

    def append_new_point_and_param(self, i_point: Reference, i_param: int) -> None:
        return self.hybrid_shape_integrated_law.AppendNewPointAndParam(
            i_point.com_object, i_param
        )

    def get_point_and_param(
        self, i_pos: int, o_point: Reference, o_param: Reference
    ) -> None:
        return self.hybrid_shape_integrated_law.GetPointAndParam(
            i_pos, o_point.com_object, o_param.com_object
        )

    def get_size(self) -> int:
        return self.hybrid_shape_integrated_law.GetSize()

    def remove_all_points_and_params(self) -> None:
        return self.hybrid_shape_integrated_law.RemoveAllPointsAndParams()

    def remove_point_and_param(self, i_point: Reference) -> None:
        return self.hybrid_shape_integrated_law.RemovePointAndParam(i_point.com_object)

    def set_end_param(self, i_end_param: int) -> None:
        return self.hybrid_shape_integrated_law.SetEndParam(i_end_param)

    def set_start_param(self, i_start_param: int) -> None:
        return self.hybrid_shape_integrated_law.SetStartParam(i_start_param)

    def __repr__(self):
        return f'HybridShapeIntegratedLaw(name="{self.name}")'

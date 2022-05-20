from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class AutoFillet(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.auto_fillet = com_object

    @property
    def curvature_radius(self) -> Length:
        return Length(self.auto_fillet.CurvatureRadius)

    @property
    def faces_to_fillet(self) -> References:
        return References(self.auto_fillet.FacesToFillet)

    @property
    def faces_to_fillets(self) -> None:
        return self.auto_fillet.FacesToFillets

    @faces_to_fillets.setter
    def faces_to_fillets(self, reference: Reference):
        self.auto_fillet.FacesToFillets = reference.com_object

    @property
    def fillet_radius(self) -> Length:
        return Length(self.auto_fillet.FilletRadius)

    @property
    def functional_face(self):
        self.functional_face.FunctionFace  # type: ignore

    @functional_face.setter
    def functional_face(self, reference: Reference):
        self.auto_fillet.FunctionalFace = reference.com_object

    @property
    def functional_faces(self) -> References:
        return References(self.auto_fillet.FunctionalFaces)

    @property
    def parting_element(self) -> Reference:
        return Reference(self.auto_fillet.PartingElement)

    @parting_element.setter
    def parting_element(self, reference: Reference):
        self.auto_fillet.PartingElement = reference.com_object

    @property
    def round_radius(self) -> Length:
        return Length(self.auto_fillet.RoundRadius)

    @property
    def round_radius_activation(self) -> bool:
        return self.auto_fillet.RoundRadiusActivation

    @round_radius_activation.setter
    def round_radius_activation(self, value: bool):
        self.auto_fillet.RoundRadiusActivation = value

    @property
    def slivers_and_crack(self) -> None:
        return self.auto_fillet.SliversAndCrack

    @slivers_and_crack.setter
    def slivers_and_crack(self, reference: Reference):
        self.auto_fillet.SliversAndCrack = reference.com_object

    @property
    def slivers_and_cracks(self) -> References:
        return References(self.auto_fillet.SliversAndCracks)

    @property
    def support_surface(self) -> Reference:
        return Reference(self.auto_fillet.SupportSurface)

    @support_surface.setter
    def support_surface(self, reference: Reference):
        self.auto_fillet.SupportSurface = reference.com_object

    def __repr__(self):
        return f'AutoFillet(name="{ self.name }")'

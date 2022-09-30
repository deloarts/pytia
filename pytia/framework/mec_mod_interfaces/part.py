from pathlib import Path
from pytia.exceptions import PytiaApplicationError
from pytia.framework.hybrid_shape_interfaces.hybrid_shape_factory import (
    HybridShapeFactory,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.parameters import Parameters
from pytia.framework.knowledge_interfaces.relations import Relations
from pytia.framework.mec_mod_interfaces.axis_systems import AxisSystems
from pytia.framework.mec_mod_interfaces.bodies import Bodies
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.mec_mod_interfaces.constraints import Constraints
from pytia.framework.mec_mod_interfaces.factory import Factory
from pytia.framework.mec_mod_interfaces.geometric_elements import GeometricElements
from pytia.framework.mec_mod_interfaces.hybrid_bodies import HybridBodies
from pytia.framework.mec_mod_interfaces.ordered_geometrical_sets import (
    OrderedGeometricalSets,
)
from pytia.framework.mec_mod_interfaces.origin_elements import OriginElements
from pytia.framework.part_interfaces.shape_factory import ShapeFactory
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.product_structure_interfaces.analyze import Analyze
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.tps_interfaces.annotation_sets import AnnotationSets


class Part(AnyObject):
    def __init__(self, com_part_object):
        super().__init__(com_part_object)
        self.part = com_part_object
        self.com_object = com_part_object

    @property
    def analyze(self) -> Analyze:
        return Analyze(self.part.Analyze)

    @property
    def annotation_sets(self) -> Collection:
        return AnnotationSets(self.part.AnnotationSets)

    @property
    def axis_systems(self) -> AxisSystems:
        return AxisSystems(self.part.AxisSystems)

    @property
    def bodies(self) -> Bodies:
        return Bodies(self.part.Bodies)

    @property
    def constraints(self) -> Constraints:
        return Constraints(self.part.Constraints)

    @property
    def density(self) -> float:
        return self.part.Density

    @property
    def file_name(self) -> str:
        try:
            return self.part.ReferenceProduct.Parent.Name
        except AttributeError:
            return self.part.Name

    @property
    def full_name(self) -> str:
        try:
            return self.part.ReferenceProduct.Parent.FullName
        except AttributeError:
            return self.part.FullName

    @property
    def geometric_elements(self) -> GeometricElements:
        return GeometricElements(self.part.GeometricElements)

    @property
    def hybrid_bodies(self) -> HybridBodies:
        return HybridBodies(self.part.HybridBodies)

    @property
    def hybrid_shape_factory(self) -> HybridShapeFactory:
        return HybridShapeFactory(self.part.HybridShapeFactory)

    @property
    def in_work_object(self) -> AnyObject:
        return AnyObject(self.part.InWorkObject)

    @in_work_object.setter
    def in_work_object(self, any_object: AnyObject):
        self.part.InWorkObject = any_object.com_object

    @property
    def main_body(self) -> Body:
        return Body(self.part.MainBody)

    @main_body.setter
    def main_body(self, body: Body):
        self.part.MainBody = body.com_object

    @property
    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        return OrderedGeometricalSets(self.part.OrderedGeometricalSets)

    @property
    def origin_elements(self) -> OriginElements:
        return OriginElements(self.part.OriginElements)

    @property
    def parameters(self) -> Parameters:
        return Parameters(self.part.Parameters)

    @property
    def relations(self) -> Relations:
        return Relations(self.part.Relations)

    @property
    def shape_factory(self) -> ShapeFactory:
        return ShapeFactory(self.part.ShapeFactory)

    @property
    def sheet_metal_factory(self) -> Factory:
        return Factory(self.part.SheetMetalFactory)

    @property
    def sheet_metal_parameters(self) -> AnyObject:
        return AnyObject(self.part.SheetMetalParameters)

    @property
    def user_surfaces(self) -> Collection:
        return Collection(self.part.UserSurfaces)

    def activate(self, i_object: AnyObject) -> None:
        return self.part.Activate(i_object.com_object)

    def create_reference_from_b_rep_name(
        self, i_label: str, i_object_context: AnyObject
    ):
        return Reference(
            self.part.CreateReferenceFromBRepName(i_label, i_object_context.com_object)
        )

    def create_reference_from_name(self, i_label: str):
        return Reference(self.part.CreateReferenceFromName(i_label))

    def create_reference_from_object(self, i_object: AnyObject):
        return Reference(self.part.CreateReferenceFromObject(i_object.com_object))

    def deactivate(self, i_object: AnyObject) -> None:
        return self.part.Inactivate(i_object.com_object)

    def find_object_by_name(self, i_obj_name: str) -> AnyObject:
        if self.part.FindObjectByName(i_obj_name):
            return AnyObject(self.part.FindObjectByName(i_obj_name))
        else:
            raise PytiaApplicationError("Could not find object.")

    def get_customer_factory(self, i_factory_iid: str) -> Factory:
        return Factory(self.part.GetCustomerFactory(i_factory_iid))

    def inactivate(self, i_object: AnyObject) -> None:
        return self.part.Inactivate(i_object.com_object)

    def is_inactive(self, i_object: AnyObject) -> bool:
        return self.part.IsInactive(i_object.com_object)

    def is_up_to_date(self, i_object: AnyObject) -> bool:
        return self.part.IsUpToDate(i_object.com_object)

    def path(self) -> Path:
        return Path(self.full_name)

    def update(self) -> None:
        return self.part.Update()

    def update_object(self, i_object: AnyObject) -> None:
        return self.part.UpdateObject(i_object.com_object)

    def __repr__(self):
        return f'Part(name="{self.name}")'

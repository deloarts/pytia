import warnings
from pathlib import Path
from typing import TYPE_CHECKING

from pytia.exceptions import PytiaApplicationError
from pytia.framework.in_interfaces.move import Move
from pytia.framework.in_interfaces.position import Position
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.parameters import Parameters
from pytia.framework.knowledge_interfaces.relations import Relations
from pytia.framework.mec_mod_interfaces.constraints import Constraints
from pytia.framework.product_structure_interfaces.analyze import Analyze
from pytia.framework.product_structure_interfaces.publications import Publications
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.document import Document
    from pytia.framework.product_structure_interfaces.products import Products


class Product(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.product = com_object

    @property
    def analyze(self) -> Analyze:
        return Analyze(self.product.Analyze)

    @property
    def definition(self) -> str:
        return self.product.Definition

    @definition.setter
    def definition(self, value: str):
        self.product.Definition = value

    @property
    def description_instance(self) -> str:
        return self.product.DescriptionInst

    @description_instance.setter
    def description_instance(self, value: str):
        self.product.DescriptionInst = value

    @property
    def description_reference(self) -> str:
        return self.product.DescriptionRef

    @description_reference.setter
    def description_reference(self, value: str):
        self.product.DescriptionRef = value

    @property
    def file_name(self):
        return self.reference_product.parent.name

    @property
    def full_name(self):
        return self.reference_product.parent.com_object.FullName

    @property
    def move(self):
        return Move(self.product.Move)

    @property
    def nomenclature(self) -> str:
        return self.product.Nomenclature

    @nomenclature.setter
    def nomenclature(self, value: str):
        self.product.Nomenclature = value

    @property
    def parameters(self) -> Parameters:
        return Parameters(self.product.Parameters)

    @property
    def part_number(self) -> str:
        try:
            return self.product.PartNumber
        except Exception as e:
            raise PytiaApplicationError(
                f'Product "{self.name}" could not do get Product.PartNumber. Check Product for broken links.'
            )

    @part_number.setter
    def part_number(self, value: str):
        try:
            self.product.PartNumber = value
        except Exception as e:
            raise PytiaApplicationError(
                f'Product "{self.name}" could not do set Product.PartNumber. Check Product for broken links.'
            )

    @property
    def position(self) -> Position:
        return Position(self.product.Position)

    @property
    def products(self) -> "Products":
        from pytia.framework.product_structure_interfaces.products import Products

        return Products(self.product.Products)

    @property
    def publications(self) -> Publications:
        return Publications(self.product.Publications)

    @property
    def reference_product(self) -> "Product":
        try:
            return Product(self.product.ReferenceProduct)
        except Exception as e:
            raise PytiaApplicationError(
                f'Product "{self.name}" could not do get Reference Product. Check Product for broken links.'
            )

    @property
    def relations(self) -> Relations:
        return Relations(self.product.Relations)

    @property
    def revision(self) -> str:
        return self.product.Revision

    @revision.setter
    def revision(self, value: str):
        self.product.Revision = value

    @property
    def source(self) -> int:
        try:
            return self.product.Source
        except Exception as e:
            raise PytiaApplicationError(
                f'Product "{self.name}" could not do get Product.Source. Check Product for broken links.'
            )

    @source.setter
    def source(self, value: int):
        try:
            self.product.Source = value
        except Exception as e:
            raise PytiaApplicationError(
                f'Product "{self.name}" could not do set Product.Source. Check Product for broken links.'
            )

    @property
    def type(self) -> str:
        root_product_name = self.reference_product.com_object.Parent.Product.Name
        self_product_name = self.reference_product.name
        if root_product_name == self_product_name:
            return self.reference_product.com_object.Parent.Name.split(".")[-1]
        else:
            return "Component"

    @property
    def user_ref_properties(self) -> Parameters:
        return Parameters(self.product.UserRefProperties)

    def activate_default_shape(self) -> None:
        return self.product.ActivateDefaultShape()

    def activate_shape(self, shape_name: str) -> None:
        return self.product.ActivateShape(shape_name)

    @staticmethod
    def activate_terminal_node(products):
        def loop_d_loop(products_):
            for product in products_:
                if product.is_catpart():
                    product.activate_default_shape()
                elif product.is_catproduct():
                    loop_d_loop(product.get_products())

        loop_d_loop(products)

    def add_master_shape_representation(self, i_shape_path_name=None):
        return self.product.AddMasterShapeRepresentation(i_shape_path_name)

    def add_shape_representation(
        self,
        i_shape_path_name: str,
        i_shape_name: str,
        i_rep_behavior: int,
        i_context: bool,
    ) -> None:
        return self.product.AddShapeRepresentation(
            i_shape_path_name, i_shape_name, i_rep_behavior, i_context
        )

    def apply_work_mode(self, new_mode: int) -> None:
        return self.product.ApplyWorkMode(new_mode)

    def attributes(self):
        return (
            "(Product) Attributes... \n"
            f"File Name:             {self.file_name}\n"
            f"Name:                  {self.name}\n"
            f"Part Number:           {self.part_number}\n"
            f"Revision:              {self.revision}\n"
            f"Definition:            {self.definition}\n"
            f"Nomenclature:          {self.nomenclature}\n"
            f"Description Instance:  {self.description_instance}\n"
            f"Description Reference: {self.description_reference}\n"
            f"Reference:             {self.reference_product}\n"
            f"Is CATProduct:         {self.is_catproduct()}\n"
            f"Is CATPart:            {self.is_catpart()}"
        )

    def constraints(self) -> Constraints:
        return Constraints(self.product.Connections("CATIAConstraints"))

    def create_reference_from_name(self, i_label: str) -> Reference:
        return Reference(self.product.CreateReferenceFromName(i_label))

    def desactivate_default_shape(self) -> None:
        return self.product.DesactivateDefaultShape()

    def desactivate_shape(self, shape_name: str) -> None:
        return self.product.DesactivateShape(shape_name)

    def extract_bom(self, i_file_type: int, i_file: str) -> None:
        return self.product.ExtractBOM(i_file_type, i_file)

    def count_children(self):
        return self.product.Products.Count

    @staticmethod
    def generate_ALLCATPart(product: "Product") -> "Document":
        from pytia.framework.in_interfaces.document import Document

        part = product.com_object.GetItem("DECProductToPart")
        part.Run()
        part = part.GetResult()
        return Document(part)

    def get_active_shape_name(self):
        return self.product.GetActiveShapeName()

    def get_all_shapes_names(self, olistshape: tuple) -> None:
        return self.product.GetAllShapesNames(olistshape)

    def get_child(self, index):
        return Product(self.product.Products.Item(index + 1))

    def get_children(self):
        children = list()
        if self.has_children():
            for i in range(self.product.Products.Count):
                child = Product(self.product.Products.Item(i + 1))
                children.append(child)
        return children

    def get_default_shape_name(self):
        return self.product.GetDefaultShapeName()

    def get_master_shape_representation(self, i_load_if_necessary: bool) -> AnyObject:
        return self.product.GetMasterShapeRepresentation(i_load_if_necessary)

    def get_master_shape_representation_path_name(self) -> str:
        return self.product.GetMasterShapeRepresentationPathName()

    def get_number_of_shapes(self) -> int:
        return self.product.GetNumberOfShapes()

    def get_products(self):
        warnings.warn(
            "This method will be deprecated in a future release. Use Product.products instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        products_ = []
        for i in range(0, self.product.Products.Count):
            product = Product(self.product.Products.Item(i + 1))
            products_.append(product)
        return products_

    def get_shape_path_name(self, i_shape_name=None):
        return self.product.GetShapePathName(i_shape_name)

    def get_shape_representation(
        self,
        i_load_if_necessary: bool,
        i_shape_name: str,
        i_rep_behavior: int,
        i_context: bool,
    ) -> AnyObject:
        return self.product.GetShapeRepresentation(
            i_load_if_necessary, i_shape_name, i_rep_behavior, i_context
        )

    def get_technological_object(self, i_application_type: str) -> AnyObject:
        return self.product.GetTechnologicalObject(i_application_type)

    def has_a_master_shape_representation(self) -> bool:
        return self.product.HasAMasterShapeRepresentation()

    def has_children(self):
        if self.product.Products.Count > 0:
            return True
        return False

    def has_shape_representation(
        self, i_shape_name: str, i_rep_behavior: int, i_context: bool
    ) -> bool:
        return self.product.HasShapeRepresentation(
            i_shape_name, i_rep_behavior, i_context
        )

    def is_catproduct(self):
        if "catproduct" == self.file_name.rsplit(".")[-1].lower():
            return True
        return False

    def is_catpart(self):
        if "catpart" == self.file_name.rsplit(".")[-1].lower():
            return True
        return False

    def path(self):
        return Path(self.full_name)

    def remove_master_shape_representation(self) -> None:
        return self.product.RemoveMasterShapeRepresentation()

    def remove_shape_representation(
        self, i_shape_name: str, i_rep_behavior: int, i_context: bool
    ) -> None:
        return self.product.RemoveShapeRepresentation(
            i_shape_name, i_rep_behavior, i_context
        )

    def update(self) -> None:
        return self.product.Update()

    def __repr__(self):
        return f'Product(name="{self.name}")'

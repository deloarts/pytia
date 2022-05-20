from pytia.framework.cat_mat_interfaces.material import Material
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.mec_mod_interfaces.hybrid_body import HybridBody
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject


class MaterialManager(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_manager = com_object

    def apply_material_on_body(
        self, i_body: Body, i_material: Material | None, i_link_mode: int = 0
    ) -> None:
        self.material_manager.ApplyMaterialOnBody(
            i_body.com_object,
            None if i_material is None else i_material.com_object,
            i_link_mode,
        )

    def apply_material_on_hybrid_body(
        self,
        i_hybrid_body: HybridBody,
        i_material: Material | None,
        i_link_mode: int = 0,
    ) -> None:
        self.material_manager.ApplyMaterialOnHybridBody(
            i_hybrid_body.com_object,
            None if i_material is None else i_material.com_object,
            i_link_mode,
        )

    def apply_material_on_part(
        self, i_part: Part, i_material: Material | None, i_link_mode: int = 0
    ) -> None:
        self.material_manager.ApplyMaterialOnPart(
            i_part.com_object,
            None if i_material is None else i_material.com_object,
            i_link_mode,
        )

    def apply_material_on_product(
        self,
        i_product: Product,
        i_material: Material | None,
        i_link_mode: int = 0,
    ) -> None:
        self.material_manager.ApplyMaterialOnProduct(
            i_product.com_object,
            None if i_material is None else i_material.com_object,
            i_link_mode,
        )

    def apply_material_on_user_material(
        self,
        i_user_material: AnyObject,
        i_material: Material | None,
        i_link_mode: int = 0,
    ) -> None:
        self.material_manager.ApplyMaterialOnUserMaterial(
            i_user_material,
            None if i_material is None else i_material.com_object,
            i_link_mode,
        )

    def get_material_on_body(self, i_body: Body) -> Material:
        vba_function_name = "get_material_on_body"
        vba_code = f"""        
        Public Function {vba_function_name}(material_manager, body)
            Dim material
            material_manager.GetMaterialOnBody body, material
            Set {vba_function_name} = material
        End Function
        """
        system_service = self.application.system_service
        return Material(
            system_service.evaluate(
                vba_code, 0, vba_function_name, [self.com_object, i_body.com_object]
            )
        )

    def get_material_on_hybrid_body(self, i_hybrid_body: HybridBody) -> Material:
        vba_function_name = "get_material_on_hybrid_body"
        vba_code = f"""        
        Public Function {vba_function_name}(material_manager, hybrid_body)
            Dim material
            material_manager.GetMaterialOnHybridBody hybrid_body, material
            Set {vba_function_name} = material
        End Function
        """
        system_service = self.application.system_service
        return Material(
            system_service.evaluate(
                vba_code,
                0,
                vba_function_name,
                [self.com_object, i_hybrid_body.com_object],
            )
        )

    def get_material_on_part(self, i_part: Part) -> Material:
        vba_function_name = "get_material_on_part"
        vba_code = f"""        
        Public Function {vba_function_name}(material_manager, part)
            Dim material
            material_manager.GetMaterialOnPart part, material
            Set {vba_function_name} = material
        End Function
        """
        system_service = self.application.system_service
        return Material(
            system_service.evaluate(
                vba_code, 0, vba_function_name, [self.com_object, i_part.com_object]
            )
        )

    def get_material_on_product(self, i_product: Product) -> Material:
        vba_function_name = "get_material_on_product"
        vba_code = f"""        
        Public Function {vba_function_name}(material_manager, product)
            Dim material
            material_manager.GetMaterialOnProduct product, material
            Set {vba_function_name} = material
        End Function
        """
        system_service = self.application.system_service
        return Material(
            system_service.evaluate(
                vba_code, 0, vba_function_name, [self.com_object, i_product.com_object]
            )
        )

    def get_material_on_user_material(self, i_user_material: AnyObject) -> Material:
        vba_function_name = "get_material_on_user_material"
        vba_code = f"""        
        Public Function {vba_function_name}(material_manager, user_material)
            Dim material
            material_manager.GetMaterialOnUserMaterial user_material, material
            Set {vba_function_name} = material
        End Function
        """
        system_service = self.application.system_service
        return Material(
            system_service.evaluate(
                vba_code,
                0,
                vba_function_name,
                [self.com_object, i_user_material.com_object],
            )
        )

    def replace_material_links(
        self, i_material1: Material, i_material2: Material
    ) -> None:
        self.material_manager.ReplaceMaterialLinks(i_material1, i_material2)

    def __repr__(self):
        return f'MaterialManager(name="{ self.name }")'

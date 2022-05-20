from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject


class AssemblyConvertor(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_convertor = com_object

    def print(self, i_file_type: str, i_file: str, i_product: Product) -> None:
        vba_function_name = "print"
        vba_code = f"""
        Public Function {vba_function_name}(assembly_convertor, i_file_type, i_file, i_product)
            assembly_convertor.Print i_file_type, i_file, i_product
            {vba_function_name} = iFileType
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code,
            0,
            vba_function_name,
            [self.com_object, i_file_type, i_file, i_product.com_object],
        )

    def set_current_format(self, ilist_props: tuple) -> None:
        return self.assembly_convertor.SetCurrentFormat(ilist_props)

    def set_secondary_format(self, ilist_props: tuple) -> None:
        return self.assembly_convertor.SetSecondaryFormat(ilist_props)

    def __repr__(self):
        return f'AssemblyConvertor(name="{self.name}")'

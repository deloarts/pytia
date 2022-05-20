from pytia.framework.system_interfaces.any_object import AnyObject


class SystemConfiguration(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.system_configuration = com_object

    @property
    def operating_system(self) -> str:
        return self.system_configuration.OperatingSystem

    @property
    def product_count(self) -> int:
        return self.system_configuration.ProductCount

    @property
    def release(self) -> int:
        return self.system_configuration.Release

    @property
    def service_pack(self) -> int:
        return self.system_configuration.ServicePack

    @property
    def version(self) -> int:
        return self.system_configuration.Version

    def get_product_names(self) -> None:
        vba_function_name = "get_product_names"
        vba_code = """
        Public Function get_product_names(system_configuration)
            ReDim ioProductNames (system_configuration.ProductCount-1)
            system_configuration.GetProductNames ioProductNames
            get_product_names = ioProductNames
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def is_product_authorized(self, i_product_name: str) -> bool:
        return self.system_configuration.IsProductAuthorized(i_product_name)

    def __repr__(self):
        return f'SystemConfiguration(name="{self.name}")'

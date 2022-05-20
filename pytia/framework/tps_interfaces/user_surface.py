from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.product_structure_interfaces.product import Product


class UserSurface(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_surface = com_object

    def add_reference(self, i_support: Reference) -> None:
        return self.user_surface.AddReference(i_support.com_object)

    def add_reference_in_a_product_ctx(
        self, i_prod_inst: Product, i_support: Reference
    ) -> None:
        return self.user_surface.AddReferenceInAProductCtx(
            i_prod_inst.com_object, i_support.com_object
        )

    def add_user_surface(self, i_user_surf: "UserSurface") -> None:
        return self.user_surface.AddUserSurface(i_user_surf.com_object)

    def __repr__(self):
        return f'UserSurface(name="{self.name}")'

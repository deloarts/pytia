from typing import Iterator
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.tps_interfaces.user_surface import UserSurface
from pytia.framework.cat_types.general import cat_variant


class UserSurfaces(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_surfaces = com_object

    def generate(self, i_support: Reference) -> UserSurface:
        return UserSurface(self.user_surfaces.Generate(i_support.com_object))

    def generate_in_a_product_ctx(
        self, i_product: Product, i_prod_inst: Product, i_support: Reference
    ) -> UserSurface:
        return UserSurface(
            self.user_surfaces.GenerateInAProductCtx(
                i_product.com_object, i_prod_inst.com_object, i_support.com_object
            )
        )

    def item(self, i_index: cat_variant) -> UserSurface:
        return UserSurface(self.user_surfaces.Item(i_index))

    def make_user_surface_node(
        self, i_first_user_surf: UserSurface, i_second_user_surf: UserSurface
    ) -> UserSurface:
        return UserSurface(
            self.user_surfaces.MakeUserSurfaceNode(
                i_first_user_surf.com_object, i_second_user_surf.com_object
            )
        )

    def make_user_surface_node_2(self, i_list_of_user_surfaces: tuple) -> UserSurface:
        return UserSurface(
            self.user_surfaces.MakeUserSurfaceNode2(i_list_of_user_surfaces)
        )

    def __getitem__(self, n: int) -> UserSurface:
        if (n + 1) > self.count:
            raise StopIteration
        return UserSurface(self.user_surfaces.item(n + 1))

    def __iter__(self) -> Iterator[UserSurface]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'UserSurfaces(name="{self.name}")'

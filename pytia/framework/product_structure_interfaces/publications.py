from typing import Iterator
from typing import TYPE_CHECKING
from pytia.framework.product_structure_interfaces.publication import Publication
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.reference import Reference


class Publications(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.publications = com_object

    def add(self, i_public_name: str) -> Publication:
        return Publication(self.publications.Add(i_public_name))

    def item(self, i_identifier: cat_variant) -> Publication:
        return Publication(self.publications.Item(i_identifier))

    def remove(self, i_identifier: str) -> None:
        return self.publications.Remove(i_identifier)

    def set_direct(self, i_identifier: cat_variant, i_pointed: "Reference") -> None:
        return self.publications.SetDirect(i_identifier, i_pointed.com_object)

    def set_relay(
        self,
        i_identifier: cat_variant,
        i_relayer: "Publications",
        i_name_in_relay: cat_variant,
    ) -> None:
        return self.publications.SetRelay(
            i_identifier, i_relayer.com_object, i_name_in_relay
        )

    def __getitem__(self, n: int) -> Publication:
        if (n + 1) > self.count:
            raise StopIteration
        return Publication(self.publications.item(n + 1))

    def __iter__(self) -> Iterator[Publication]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Publications(name="{self.name}")'

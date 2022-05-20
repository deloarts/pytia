from typing import Iterator
from pytia.framework.part_interfaces.draft_domain import DraftDomain
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class DraftDomains(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.draft_domains = com_object

    def item(self, i_index: cat_variant) -> DraftDomain:
        return DraftDomain(self.draft_domains.Item(i_index))

    def __getitem__(self, n: int) -> DraftDomain:
        if (n + 1) > self.count:
            raise StopIteration
        return DraftDomain(self.draft_domains.item(n + 1))

    def __iter__(self) -> Iterator[DraftDomain]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DraftDomains(name="{self.name}")'

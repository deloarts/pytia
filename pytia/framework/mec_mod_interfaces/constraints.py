from typing import Iterator
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.constraint import Constraint
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Constraints(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Constraint)
        self.constraints = com_object

    @property
    def broken_constraints_count(self) -> int:
        return self.constraints.BrokenConstraintsCount

    @property
    def un_updated_constraints_count(self) -> int:
        return self.constraints.UnUpdatedConstraintsCount

    def add_bi_elt_cst(
        self, i_cst_type: int, i_first_elem: Reference, i_second_elem: Reference
    ) -> Constraint:
        return Constraint(
            self.constraints.AddBiEltCst(
                i_cst_type, i_first_elem.com_object, i_second_elem.com_object
            )
        )

    def add_mono_elt_cst(self, i_cst_type: int, i_elem: Reference) -> Constraint:
        return Constraint(self.constraints.AddMonoEltCst(i_cst_type, i_elem.com_object))

    def add_tri_elt_cst(
        self,
        i_cst_type: int,
        i_first_elem: Reference,
        i_second_elem: Reference,
        i_third_elem: Reference,
    ) -> Constraint:
        return Constraint(
            self.constraints.AddTriEltCst(
                i_cst_type,
                i_first_elem.com_object,
                i_second_elem.com_object,
                i_third_elem.com_object,
            )
        )

    def item(self, i_index: cat_variant) -> Constraint:
        return Constraint(self.constraints.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.constraints.Remove(i_index)

    def __getitem__(self, n: int) -> Constraint:
        if (n + 1) > self.count:
            raise StopIteration
        return Constraint(self.constraints.item(n + 1))

    def __iter__(self) -> Iterator[Constraint]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Constraints(name="{self.name}")'

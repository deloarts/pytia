from typing import Iterator
from pytia.framework.knowledge_interfaces.optimization import Optimization
from pytia.framework.knowledge_interfaces.set_of_equation import SetOfEquation
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Optimizations(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Optimization)
        self.optimizations = com_object

    def create_constraints_satisfaction(
        self, i_name: str, i_comment: str, i_formula_body: str
    ) -> SetOfEquation:
        return SetOfEquation(
            self.optimizations.CreateConstraintsSatisfaction(
                i_name, i_comment, i_formula_body
            )
        )

    def create_optimization(self) -> Optimization:
        return Optimization(self.optimizations.CreateOptimization())

    def item(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.optimizations.Item(i_index))

    def __getitem__(self, n: int) -> Optimization:
        if (n + 1) > self.count:
            raise StopIteration
        return Optimization(self.optimizations.item(n + 1))

    def __iter__(self) -> Iterator[Optimization]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Optimizations(name="{self.name}")'
